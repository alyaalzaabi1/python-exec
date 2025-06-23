import asyncio
from plugin_manager import PluginManager

async def run_plugins(text: str):
    manager = PluginManager()
    manager.load_plugins()
    results = {}

    for plugin in manager.get_plugins():
        print(f"\nRunning {plugin.name} v{plugin.version}...")
        try:
            if plugin.is_async:
                res = await plugin.analyze_async(text)
            else:
                res = plugin.analyze(text)
            results[plugin.name] = res
        except Exception as e:
            print(f"Failed: {e}")

    print("\n--- Final Results ---")
    for name, res in results.items():
        print(f"{name}: {res}")

text = "This is a good example for plugin design in Python."
asyncio.run(run_plugins(text))
