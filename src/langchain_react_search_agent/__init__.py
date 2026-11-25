AGENT = "tavily_tool"


def main() -> None:
    match AGENT:
        case "custom_tool":
            from langchain_react_search_agent.custom_tool import main as run
        case "tavily_tool":
            from langchain_react_search_agent.tavily_tool import main as run
        case _:
            raise ValueError(
                f"Unknown AGENT {AGENT!r}; use 'custom_tool' or 'tavily_tool'"
            )
    run()


if __name__ == "__main__":
    main()
