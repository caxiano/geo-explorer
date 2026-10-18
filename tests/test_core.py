import pytest

from geo_explorer.core import certificate, challenge, find_track, trail


def test_find_track_is_case_insensitive():
    assert find_track("python", "INICIANTE").technology == "Python"


def test_trail_lists_all_modules():
    result = trail("Python", "iniciante")
    assert "1. Lógica e sintaxe" in result
    assert "4. Arquivos e testes" in result


def test_challenge_depends_on_technology():
    assert "números pares" in challenge("Python", "iniciante")
    assert "produtos" in challenge("JavaScript", "iniciante")


def test_certificate_rejects_empty_name():
    with pytest.raises(ValueError, match="obrigatório"):
        certificate("", "Python", "iniciante")


def test_unknown_track_has_actionable_error():
    with pytest.raises(ValueError, match="não encontrada"):
        trail("Go", "iniciante")
