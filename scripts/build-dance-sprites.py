"""Build a centered 32-frame loop from the approved Brazilian 8-count poses."""

from pathlib import Path
import sys

from PIL import Image


CELL = 256
SOURCE_COLUMNS = 4
SOURCE_ROWS = 2
OUTPUT_COLUMNS = 8
INBETWEENS = 4


def extract_poses(source):
    poses = []
    for row in range(SOURCE_ROWS):
        top = round(row * source.height / SOURCE_ROWS)
        bottom = round((row + 1) * source.height / SOURCE_ROWS)
        for column in range(SOURCE_COLUMNS):
            left = round(column * source.width / SOURCE_COLUMNS)
            right = round((column + 1) * source.width / SOURCE_COLUMNS)
            frame = source.crop((left, top, right, bottom))
            alpha = frame.getchannel("A")
            bounds = alpha.point(lambda value: 255 if value >= 20 else 0).getbbox()
            if not bounds:
                raise RuntimeError(f"Empty pose at {column}, {row}")
            poses.append(frame.crop(bounds))
    return poses


def normalize_poses(poses):
    max_width = max(pose.width for pose in poses)
    max_height = max(pose.height for pose in poses)
    scale = min(218 / max_width, 238 / max_height)
    normalized = []
    for pose in poses:
        resized = pose.resize(
            (round(pose.width * scale), round(pose.height * scale)),
            Image.Resampling.NEAREST,
        )
        frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
        x = (CELL - resized.width) // 2
        y = 246 - resized.height
        frame.alpha_composite(resized, (x, y))
        normalized.append(frame)
    return normalized


def interpolate(poses):
    frames = []
    for index, current in enumerate(poses):
        following = poses[(index + 1) % len(poses)]
        for step in range(INBETWEENS):
            amount = step / INBETWEENS
            frames.append(Image.blend(current, following, amount))
    return frames


def pack(frames, output_path):
    rows = (len(frames) + OUTPUT_COLUMNS - 1) // OUTPUT_COLUMNS
    sheet = Image.new("RGBA", (OUTPUT_COLUMNS * CELL, rows * CELL), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        x = (index % OUTPUT_COLUMNS) * CELL
        y = (index // OUTPUT_COLUMNS) * CELL
        sheet.alpha_composite(frame, (x, y))
    sheet.save(output_path, optimize=True)


def main(source_path, output_path):
    source = Image.open(source_path).convert("RGBA")
    poses = normalize_poses(extract_poses(source))
    pack(interpolate(poses), output_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: build-dance-sprites.py SOURCE OUTPUT")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
