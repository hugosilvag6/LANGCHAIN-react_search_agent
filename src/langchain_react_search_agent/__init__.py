AGENT = "custom_tool"


def main() -> None:
    match AGENT:
        case "custom_tool":
            from .custom_tool import main as run
        case "tavily_tool":
            from .tavily_tool import main as run
        case _:
            raise ValueError(
                f"Unknown AGENT {AGENT!r}; use 'custom_tool' or 'tavily_tool'"
            )
    run()


if __name__ == "__main__":
    main()
