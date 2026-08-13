import json
from pathlib import Path


class DatasetExporter:

    def export_json(self, pairs, output_path):

        data = []

        for pair in pairs:
            data.append({
                "context": pair.context,
                "response": pair.response
            })

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"\nSaved {len(data)} pairs to {output}")