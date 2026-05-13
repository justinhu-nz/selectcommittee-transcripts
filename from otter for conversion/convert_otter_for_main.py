from __future__ import annotations

import json
import re
import shutil
import textwrap
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "ready_for_main_directory"


HEADER_RE = re.compile(r"^(?P<speaker>.+?)\s{2,}(?P<stamp>(?:\d+:)?\d{1,2}:\d{2})$")


ITEMS = [
    {
        "source_file": "2025_12_02_-_fec_(part_1) (240p).txt",
        "folder": "2025 12 02 - FEC (Part 1) - vimeo_1140980470",
        "base": "2025 12 02 - FEC (Part 1) - vimeo_1140980470",
        "title": "2025 12 02 - FEC (Part 1)",
        "media_id": "vimeo_1140980470",
        "vimeo_id": "1140980470",
        "url": "https://vimeo.com/1140980470",
        "published": "2025-12-02",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "description": (
            "Tuesday 2 December 2025 | Finance and Expenditure Committee\n\n"
            "Financial Statements of the Government of New Zealand for the year ended 30 June 2025\n\n"
            "Hearing of evidence:\n\n"
            "Hon Nicola Willis, Minister of Finance\n\n"
            "The Treasury\n\n"
            "Iain Rennie, CNZM - Secretary to the Treasury and Chief Executive\n"
            "Janyne Winfield, Chief Government Accountant"
        ),
    },
    {
        "source_file": "2025_12_02_-_fec_(part_3) (240p).txt",
        "folder": "2025 12 02 - FEC (Part 3) - vimeo_1142227704",
        "base": "2025 12 02 - FEC (Part 3) - vimeo_1142227704",
        "title": "2025 12 02 - FEC (Part 3)",
        "media_id": "vimeo_1142227704",
        "vimeo_id": "1142227704",
        "url": "https://vimeo.com/1142227704",
        "published": "2025-12-02",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "duration_seconds": 5229,
        "description": (
            "Tuesday 2 December 2025 | Finance and Expenditure Committee\n\n"
            "2024/25 Annual review of the Ministry for Regulation\n\n"
            "Hearing of evidence:\n\n"
            "Ministry for Regulation\n\n"
            "Grainne Moss, Chief Executive\n"
            "Andrew Royle, Deputy Chief Executive - Policy\n"
            "Paula Knaap, Deputy Chief Executive - Organisational Enablement\n"
            "Kevin Counsell, Chief Economist"
        ),
    },
    {
        "source_file": "2026_01_28_fec (240p) (1).txt",
        "folder": "2026 01 28 FEC - vimeo_1147166354",
        "base": "2026 01 28 FEC - vimeo_1147166354",
        "title": "2026 01 28 FEC",
        "media_id": "vimeo_1147166354",
        "vimeo_id": "1147166354",
        "url": "https://vimeo.com/1147166354",
        "published": "2026-01-28",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "description": (
            "Wednesday 28 January 2026 | Finance and Expenditure Committee\n\n"
            "Budget Policy Statement 2026 and Half-year Economic and Fiscal Update 2025\n\n"
            "Hon Nicola Willis, Minister of Finance\n\n"
            "The Treasury\n\n"
            "Iain Rennie CNZM, Secretary to the Treasury and Chief Executive\n"
            "Chris Bunny, Deputy Secretary, Budget and Fiscal Performance"
        ),
    },
    {
        "source_file": "2026_01_28_fec (240p).txt",
        "folder": "2026 01 28 FEC - vimeo_1158961632",
        "base": "2026 01 28 FEC - vimeo_1158961632",
        "title": "2026 01 28 FEC",
        "media_id": "vimeo_1158961632",
        "vimeo_id": "1158961632",
        "url": "https://vimeo.com/1158961632",
        "published": "2026-01-28",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "description": (
            "Wednesday 28 January 2026 | Finance and Expenditure Committee\n\n"
            "The Treasury, Te Ara Mokopuna, 2025 Long-term Insights Briefing\n\n"
            "The Treasury, Long-term Fiscal Statement 2025\n\n"
            "He Puna Hao Pātiki Investment Statement 2025\n\n"
            "The Treasury\n\n"
            "Iain Rennie CNZM, Secretary to the Treasury and Chief Executive\n"
            "Chris Bunny, Deputy Secretary, Budget and Fiscal Performance\n"
            "Struan Little, Chief Strategist"
        ),
    },
    {
        "source_file": "2026_02_11_fec (240p).txt",
        "folder": "2026 02 11 FEC - vimeo_1163753802",
        "base": "2026 02 11 FEC - vimeo_1163753802",
        "title": "2026 02 11 FEC",
        "media_id": "vimeo_1163753802",
        "vimeo_id": "1163753802",
        "url": "https://vimeo.com/1163753802",
        "published": "2026-02-11",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "description": (
            "Wednesday 11 February 2026| Finance and Expenditure Committee\n\n"
            "Briefing on the response to the inquiry into banking competition\n\n"
            "Bank of New Zealand\n\n"
            "Warwick Hunt, Chair\n"
            "Dan Huggins, Chief Executive"
        ),
    },
    {
        "source_file": "2026_02_19_fec (240p).txt",
        "folder": "2026 02 19 FEC - vimeo_1165853682",
        "base": "2026 02 19 FEC - vimeo_1165853682",
        "title": "2026 02 19 FEC",
        "media_id": "vimeo_1165853682",
        "vimeo_id": "1165853682",
        "url": "https://vimeo.com/1165853682",
        "published": "2026-02-19",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "description": (
            "Thursday 19 February 2026 | Finance and Expenditure Committee\n\n"
            "Reserve Bank of New Zealand, Monetary Policy Statement, February 2026\n\n"
            "Reserve Bank of New Zealand\n\n"
            "Dr Anna Breman, Governor\n"
            "Karen Silk, Assistant Governor, Money\n"
            "Paul Conway, Chief Economist"
        ),
    },
    {
        "source_file": "2026_03_04_fec (240p).txt",
        "folder": "2026 03 04 FEC - vimeo_1170078497",
        "base": "2026 03 04 FEC - vimeo_1170078497",
        "title": "2026 03 04 FEC",
        "media_id": "vimeo_1170078497",
        "vimeo_id": "1170078497",
        "url": "https://vimeo.com/1170078497",
        "showcase_url": "https://vimeo.com/showcase/10758103?video=1170078497",
        "published": "2026-03-04",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "duration_seconds": 5812,
        "description": (
            "Wednesday 4 March 2026 | Finance and Expenditure Committee\n\n"
            "Infrastructure Funding and Financing Amendment Bill\n\n"
            "Hearing of evidence"
        ),
    },
    {
        "source_file": "2026_03_05_-_fd_part_2 (240p).txt",
        "folder": "2026_03_05 - FD Part 2 - vimeo_1170400692",
        "base": "2026_03_05 - FD Part 2 - vimeo_1170400692",
        "title": "2026/03/05 - FD Part 2",
        "media_id": "vimeo_1170400692",
        "vimeo_id": "1170400692",
        "url": "https://vimeo.com/1170400692",
        "published": "2026-03-05",
        "showcase": "10758106",
        "source_labels": "Vimeo Showcase 10758106",
        "description": (
            "Thursday 5 March 2026 | Foreign Affairs, Defence and Trade Committee\n\n"
            "Briefing on meetings with representative counterparts and government officials\n\n"
            "Hearing of evidence\n\n"
            "Submitters List:\n\n"
            "Delegation from Vanuatu Parliament\n\n"
            "The Honourable Stephen Dorrick Felix MP, Speaker of Parliament\n"
            "The Honourable Marie Louise Paulette MP, Member of Parliament\n"
            "The Honourable Jones Malnimbwen MP, Member of Parliament\n"
            "The Honourable Danny Silas MP, Member of Parliament\n"
            "Peter Joseph, Senior Finance Officer\n"
            "Paul Zebedee Stephen, Political advisor to the Speaker\n"
            "Naklan Martiano, Security"
        ),
    },
    {
        "source_file": "2026_05_13_fec (240p).txt",
        "folder": "2026 05 13 FEC - vimeo_1189913057",
        "base": "2026 05 13 FEC - vimeo_1189913057",
        "title": "2026 05 13 FEC",
        "media_id": "vimeo_1189913057",
        "vimeo_id": "1189913057",
        "url": "https://vimeo.com/1189913057",
        "published": "2026-05-13",
        "showcase": "10758103",
        "source_labels": "Vimeo Showcase 10758103",
        "duration_seconds": 1608,
        "description": (
            "Wednesday 13 May 2026| Finance and Expenditure Committee\n"
            "Review briefing on the 2024/25 Annual review of Kiwi Group Capital Limited\n"
            "Kiwi Group Capital Limited\n"
            "David Mclean, Chair of Kiwi Group Capital\n"
            "Steve Jurkovich, Chief Executive - Kiwibank"
        ),
    },
]


def parse_stamp(stamp: str) -> float:
    parts = [int(part) for part in stamp.split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        return float(minutes * 60 + seconds)
    hours, minutes, seconds = parts
    return float(hours * 3600 + minutes * 60 + seconds)


def fmt_hms(seconds: float) -> str:
    total = int(round(seconds))
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def fmt_vtt(seconds: float) -> str:
    millis = int(round((seconds - int(seconds)) * 1000))
    whole = int(seconds)
    if millis == 1000:
        whole += 1
        millis = 0
    hours = whole // 3600
    minutes = (whole % 3600) // 60
    secs = whole % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def parse_otter(path: Path) -> list[dict[str, object]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    text_lines: list[str] = []

    def flush() -> None:
        nonlocal current, text_lines
        if current is None:
            return
        text = " ".join(line.strip() for line in text_lines if line.strip())
        text = re.sub(r"\s+", " ", text).strip()
        if text and text != "Transcribed by https://otter.ai":
            current["text"] = text
            blocks.append(current)
        current = None
        text_lines = []

    for line in lines:
        if line.strip() == "Transcribed by https://otter.ai":
            flush()
            break
        match = HEADER_RE.match(line.strip())
        if match:
            flush()
            current = {
                "speaker": match.group("speaker").strip(),
                "start": parse_stamp(match.group("stamp")),
            }
            continue
        text_lines.append(line)
    flush()

    for index, block in enumerate(blocks):
        start = float(block["start"])
        if index + 1 < len(blocks):
            next_start = float(blocks[index + 1]["start"])
            end = next_start if next_start > start else start + 1.0
        else:
            end = start + 5.0
        block["end"] = end
    return blocks


def build_source_metadata(item: dict[str, object], duration: int) -> dict[str, object]:
    vimeo_id = str(item["vimeo_id"])
    return {
        "provider": "vimeo",
        "id": vimeo_id,
        "display_id": vimeo_id,
        "title": item["title"],
        "description": item["description"],
        "webpage_url": item["url"],
        "original_url": item["url"],
        "upload_date": str(item["published"]).replace("-", ""),
        "duration": duration,
        "uploader": "New Zealand Parliament",
        "uploader_id": "nzparliament",
        "uploader_url": "https://vimeo.com/nzparliament",
        "width": 1280,
        "height": 720,
        "fps": 30,
        "extractor": "vimeo",
        "extractor_key": "Vimeo",
        "caption_language": "en-x-autogen",
        "caption_kind": "otter.ai",
        "caption_download_method": "otter_txt_export",
    }


def write_txt(path: Path, item: dict[str, object], duration: int, segments: list[dict[str, object]]) -> None:
    lines = [
        f"Title: {item['title']}",
        f"URL: {item['url']}",
        f"Published: {item['published']}",
        f"Duration: {fmt_hms(duration)}",
        "",
    ]
    for segment in segments:
        lines.append(f"[{fmt_hms(float(segment['start']))}] {segment['text']}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_vtt(path: Path, segments: list[dict[str, object]]) -> None:
    lines = ["WEBVTT", ""]
    for index, segment in enumerate(segments, start=1):
        lines.append(str(index))
        lines.append(f"{fmt_vtt(float(segment['start']))} --> {fmt_vtt(float(segment['end']))}")
        lines.extend(textwrap.wrap(str(segment["text"]), width=80) or [""])
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "output_note": "Generated from Otter.ai text exports. Speaker labels were removed to match the collection transcript style.",
        "items": [],
    }

    for item in ITEMS:
        source_path = ROOT / str(item["source_file"])
        if not source_path.exists():
            raise FileNotFoundError(source_path)

        folder = OUT / str(item["folder"])
        folder.mkdir(parents=True)

        parsed_blocks = parse_otter(source_path)
        if not parsed_blocks:
            raise ValueError(f"No transcript blocks parsed from {source_path}")

        segments = [
            {
                "start": round(float(block["start"]), 2),
                "end": round(float(block["end"]), 2),
                "text": block["text"],
            }
            for block in parsed_blocks
        ]
        parsed_duration = int(round(max(float(segment["end"]) for segment in segments)))
        known_duration = item.get("duration_seconds")
        duration = int(known_duration or parsed_duration)
        if segments:
            last_start = float(segments[-1]["start"])
            if known_duration and duration > last_start:
                segments[-1]["end"] = float(duration)
            elif not known_duration:
                segments[-1]["end"] = max(float(segments[-1]["end"]), float(duration))

        source_metadata = build_source_metadata(item, duration)
        generated_at = datetime.now(timezone.utc).isoformat()
        base = str(item["base"])
        vtt_path = folder / f"{base}.en.vtt"
        source_otter_path = str(source_path)

        transcript_json = {
            "language": "en-x-autogen",
            "duration": round(float(duration), 2),
            "segments": segments,
            "source": "otter_ai_txt",
            "source_vtt_path": str(vtt_path),
            "source_otter_path": source_otter_path,
            "source_metadata": source_metadata,
        }
        metadata_json = {
            "generated_at": generated_at,
            "provider": "vimeo",
            "media_id": item["media_id"],
            "title": item["title"],
            "url": item["url"],
            "published_at": str(item["published"]).replace("-", ""),
            "published_display": item["published"],
            "duration_seconds": duration,
            "source_labels": item["source_labels"],
            "transcript": {
                "source": "otter_ai_txt",
                "language": "en-x-autogen",
                "duration_seconds": round(float(duration), 2),
                "segment_count": len(segments),
                "source_vtt_path": str(vtt_path),
                "source_otter_path": source_otter_path,
            },
            "source_metadata": source_metadata,
        }
        if "showcase_url" in item:
            metadata_json["showcase_url"] = item["showcase_url"]

        write_txt(folder / f"{base}.txt", item, duration, segments)
        write_vtt(vtt_path, segments)
        (folder / f"{base}.json").write_text(
            json.dumps(transcript_json, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (folder / f"{base}.metadata.json").write_text(
            json.dumps(metadata_json, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        manifest["items"].append(
            {
                "source_file": item["source_file"],
                "output_folder": item["folder"],
                "media_id": item["media_id"],
                "url": item["url"],
                "segment_count": len(segments),
                "duration_seconds": duration,
            }
        )

    (OUT / "conversion_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
