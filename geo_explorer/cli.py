import argparse

from .core import certificate, challenge, trail


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="geo-explorer", description="Explore trilhas fictícias de aprendizagem.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("trilha", "Apresenta uma trilha"), ("desafio", "Gera um desafio")):
        command = sub.add_parser(name, help=help_text)
        command.add_argument("tecnologia")
        command.add_argument("nivel")
    cert = sub.add_parser("certificado", help="Gera um certificado fictício")
    cert.add_argument("nome")
    cert.add_argument("tecnologia")
    cert.add_argument("nivel")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "trilha":
            output = trail(args.tecnologia, args.nivel)
        elif args.command == "desafio":
            output = challenge(args.tecnologia, args.nivel)
        else:
            output = certificate(args.nome, args.tecnologia, args.nivel)
        print(output)
        return 0
    except ValueError as error:
        print(f"Erro: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
