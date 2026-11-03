import argparse,json
from pathlib import Path
def render(data):
 rows=["# Weekly Metrics Report","","| Metric | Value |","|---|---:|"]
 rows += [f"| {k.replace('_',' ').title()} | {v} |" for k,v in sorted(data.items())]
 return "\n".join(rows)+"\n"
def main():
 p=argparse.ArgumentParser();p.add_argument("input",nargs="?",default="metrics.json");p.add_argument("-o","--output",default="report.md");a=p.parse_args()
 Path(a.output).write_text(render(json.loads(Path(a.input).read_text())),encoding="utf-8");print("Wrote",a.output)
if __name__=="__main__":main()
