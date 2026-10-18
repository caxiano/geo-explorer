from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Track:
    technology: str
    level: str
    description: str
    modules: list[str]


def load_tracks(path: str | Path | None = None) -> list[Track]:
    source = Path(path or Path(__file__).parents[1] / "data" / "tracks.json")
    raw = json.loads(source.read_text(encoding="utf-8"))
    return [Track(**item) for item in raw]


def find_track(technology: str, level: str, tracks: list[Track] | None = None) -> Track:
    tech = technology.strip().casefold()
    lvl = level.strip().casefold()
    for track in tracks or load_tracks():
        if track.technology.casefold() == tech and track.level.casefold() == lvl:
            return track
    raise ValueError(f"Trilha não encontrada para {technology!r} no nível {level!r}.")


def trail(technology: str, level: str) -> str:
    item = find_track(technology, level)
    modules = "\n".join(f"  {index}. {module}" for index, module in enumerate(item.modules, 1))
    return f"Trilha de {item.technology} — {item.level}\n{item.description}\nMódulos:\n{modules}"


def challenge(technology: str, level: str) -> str:
    item = find_track(technology, level)
    if item.technology.casefold() == "python":
        task = "Crie uma função que receba uma lista de números e retorne apenas os números pares, em ordem."
        example = "Exemplo: [3, 8, 1, 4] -> [8, 4]"
    else:
        task = "Crie uma função que receba uma lista de produtos e retorne os nomes ordenados alfabeticamente."
        example = "Exemplo: ['Zeta', 'Alfa'] -> ['Alfa', 'Zeta']"
    return f"Desafio {item.technology} — {item.level}\n{task}\n{example}\nCritérios: solução legível, caso vazio e pelo menos um teste automatizado."


def certificate(name: str, technology: str, level: str) -> str:
    if not name.strip():
        raise ValueError("O nome é obrigatório.")
    item = find_track(technology, level)
    safe_name = re.sub(r"\s+", " ", name).strip()
    return (f"CERTIFICADO DE CONCLUSÃO\n\nCertificamos que {safe_name} concluiu a trilha "
            f"de {item.technology} ({item.level}).\n\nGeo-Explorer | certificado fictício")


def track_as_dict(track: Track) -> dict:
    return asdict(track)
