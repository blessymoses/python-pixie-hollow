# import os

# from behave.__main__ import main as behave_runner


# def run_all_feature_files(base_dir="features"):
#     # Walk through all files in the base directory
#     for root, dirs, files in os.walk(base_dir):
#         for file in files:
#             if file.endswith(".feature"):
#                 feature_path = os.path.join(root, file)
#                 print(f"\nRunning feature: {feature_path}")
#                 behave_runner(feature_path)

# if __name__ == "__main__":
#     run_all_feature_files()

import json

# run_and_combine.py
import os
from html import escape
from pathlib import Path

from behave.__main__ import main as behave_runner

FEATURE_DIR = "features"
REPORT_DIR = "reports"
COMBINED_JSON = os.path.join(REPORT_DIR, "combined.json")

def run_all_features_and_collect():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        print(f"Report dir created")
    else:
        print(f"Report dir exists")

    combined_data = []
    for root, _, files in os.walk(FEATURE_DIR):
        for file in files:
            if file.endswith(".feature"):
                feature_path = os.path.join(root, file)
                print(f"Running: {feature_path}")

                tmp_json = os.path.join(REPORT_DIR, "tmp.json")
                if os.path.exists(tmp_json):
                    os.remove(tmp_json)

                behave_runner(f"{feature_path} -f json -o {tmp_json}")
                if os.path.exists(tmp_json):
                    with open(tmp_json) as f:
                        combined_data.extend(json.load(f))

    with open(COMBINED_JSON, "w") as f:
        json.dump(combined_data, f, indent=2)

    print(f"✅ Combined report written to {COMBINED_JSON}")


# def generate_html_report(COMBINED_JSON, HTML_OUTPUT):
#     with open(COMBINED_JSON) as f:
#         data = json.load(f)

#     html_parts = [
#         "<html><head><title>Behave Report</title>",
#         "<style>body{font-family:sans-serif;} table{border-collapse:collapse;} th,td{border:1px solid #ccc;padding:5px;}</style>",
#         "</head><body><h1>Behave Test Report</h1><table>",
#         "<tr><th>Feature</th><th>Scenario</th><th>Status</th><th>Steps</th></tr>"
#     ]

#     for feature in data:
#         feature_name = feature.get("name", "")
#         for element in feature.get("elements", []):
#             scenario = element.get("name", "")
#             steps = element.get("steps", [])
#             status = "passed"
#             step_texts = []

#             for step in steps:
#                 step_status = step.get("result", {}).get("status", "undefined")
#                 step_text = f"{escape(step['keyword'])} {escape(step['name'])} ({step_status})"
#                 step_texts.append(step_text)
#                 if step_status != "passed":
#                     status = "failed"

#             html_parts.append(f"<tr><td>{escape(feature_name)}</td><td>{escape(scenario)}</td><td>{status}</td><td><ul><li>" + "</li><li>".join(step_texts) + "</li></ul></td></tr>")

#     html_parts.append("</table></body></html>")

#     Path(HTML_OUTPUT).write_text("\n".join(html_parts), encoding="utf-8")
#     print(f"✅ HTML report generated at: {HTML_OUTPUT}")

# def generate_behave_html_report(json_file_path: str, output_html_path: str) -> None:
#     with open(json_file_path) as f:
#         features = json.load(f)

#     # Summary counters
#     features_passed = 0
#     features_failed = 0
#     scenarios_passed = 0
#     scenarios_failed = 0
#     steps_passed = 0
#     steps_failed = 0
#     steps_skipped = 0
#     any_failed = False

#     html = """
# <!DOCTYPE HTML><html><head><title>Behave Test Report</title><meta content="text/html;charset=utf-8" http-equiv="content-type" />
# <style type="text/css">
# body { font-family: sans-serif; font-size: 13px; background: white; color: black; }
# .feature { margin: 20px; padding: 10px; border: 1px solid #ccc; }
# .feature h2 { color: #246ac1; }
# .scenario h3.failed { background-color: #c20000; color: white; padding: 4px; }
# .scenario h3.passed { background-color: #65c400; color: white; padding: 4px; }
# .step.failed { background-color: #fffbd3; color: #c20000; padding-left: 10px; }
# .step.passed { background-color: #dbffb4; color: #3d7700; padding-left: 10px; }
# .step.skipped { background-color: #e0ffff; padding-left: 10px; }
# pre { white-space: pre-wrap; background: #eee; padding: 5px; margin: 0 0 10px 10px; }
# </style></head><body><div class="behave">
# """

#     # Process each feature
#     for feature in features:
#         feature_html = f'<div class="feature"><h2>Feature: {feature["name"]}</h2>'
#         feature_failed = False

#         for idx, scenario in enumerate(feature.get("elements", [])):
#             scenario_status = scenario.get("status", "passed")
#             scenario_failed = scenario_status == "failed"
#             if scenario_failed:
#                 scenarios_failed += 1
#                 feature_failed = True
#                 any_failed = True
#             else:
#                 scenarios_passed += 1

#             step_list_html = ""
#             for step in scenario.get("steps", []):
#                 result = step.get("result", {})
#                 status = result.get("status", "skipped")
#                 css = f"step {status}"
#                 error_html = ""

#                 if status == "failed":
#                     steps_failed += 1
#                     error_msg = "\n".join(result.get("error_message", []))
#                     error_html = f'<pre>{error_msg}</pre>'
#                 elif status == "passed":
#                     steps_passed += 1
#                 else:
#                     steps_skipped += 1

#                 step_list_html += f'<li class="{css}">{step["keyword"]} {step["name"]}{error_html}</li>'

#             scenario_class = "failed" if scenario_failed else "passed"
#             feature_html += f'<div class="scenario"><h3 class="{scenario_class}">Scenario: {scenario["name"]}</h3><ol>{step_list_html}</ol></div>'

#         feature_html += "</div>"
#         html += feature_html

#         if feature_failed:
#             features_failed += 1
#         else:
#             features_passed += 1

#     # Summary section
#     overall_class = "failed" if any_failed else "passed"
#     html = html.replace(
#         '<div class="behave">',
#         f'<div class="behave"><div id="behave-header" class="{overall_class}">'
#         f'<h1>Behave Test Report</h1><div id="summary">'
#         f'<p>Features: passed: {features_passed}, failed: {features_failed}</p>'
#         f'<p>Scenarios: passed: {scenarios_passed}, failed: {scenarios_failed}</p>'
#         f'<p>Steps: passed: {steps_passed}, failed: {steps_failed}, skipped: {steps_skipped}</p>'
#         f'<p>Finished in 0.0 seconds</p></div></div>'
#     )

#     html += "</div></body></html>"

#     # Write to output file
#     Path(output_html_path).write_text(html)
#     print(f"✅ HTML report written to: {output_html_path}")

def extract_block(source_html: str, start_tag: str, end_tag: str) -> str:
    return source_html.split(start_tag)[1].split(end_tag)[0]


def generate_behave_html_report(combined_json_path: str, template_html_path: str, output_path: str):
    # Load data
    with open(combined_json_path) as f:
        features = json.load(f)

    # Extract style and script from template HTML
    html_template = Path(template_html_path).read_text()
    style_block = extract_block(html_template, '<style type="text/css">', "</style>")
    script_block = extract_block(html_template, '<script type="text/javascript">', "</script>")

    # Stats
    features_passed = sum(1 for f in features if f["status"] == "passed")
    features_failed = sum(1 for f in features if f["status"] == "failed")
    scenarios_passed = scenarios_failed = 0
    steps_passed = steps_failed = steps_skipped = 0

    for feature in features:
        for scenario in feature.get("elements", []):
            if scenario["status"] == "passed":
                scenarios_passed += 1
            else:
                scenarios_failed += 1
            for step in scenario.get("steps", []):
                status = step.get("result", {}).get("status")
                if status == "passed":
                    steps_passed += 1
                elif status == "failed":
                    steps_failed += 1
                elif status == "skipped":
                    steps_skipped += 1

    overall_status = "failed" if features_failed or scenarios_failed or steps_failed else "passed"

    # HTML header
    html = f"""<!DOCTYPE HTML><html><head><title>Behave Test Report</title>
<meta content="text/html;charset=utf-8" http-equiv="content-type" />
<style type="text/css">{style_block}</style>
<script type="text/javascript">{script_block}</script>
</head><body><div class="behave">
<div id="behave-header" class="{overall_status}">
<div id="label"><h1>Behave Test Report</h1></div>
<div id="summary">
<p id="totals">
<p id="feature_totals">Features: passed: {features_passed}, failed: {features_failed}</p>
<p id="scenario_totals">Scenarios: passed: {scenarios_passed}, failed: {scenarios_failed}</p>
<p id="step_totals">Steps: passed: {steps_passed}, failed: {steps_failed}, skipped: {steps_skipped}</p>
</p><p id="duration">Finished in 0.0 seconds</p>
<div id="expand-collapse">
<a id="expander" href="#" onclick="Collapsible_expandAll('scenario_steps')">Expand All</a> |
<a id="collapser" href="#" onclick="Collapsible_collapseAll('scenario_steps')">Collapse All</a> |
<a id="failed_expander" href="#" onclick="Collapsible_expandAllFailed()">Expand All Failed</a>
</div></div></div>"""

    step_counter = 0
    for feature in features:
        html += f'<div class="feature"><h2><span class="val">Feature: {escape(feature["name"])}</span></h2><span /></div>'
        for scenario in feature.get("elements", []):
            sc_status = scenario["status"]
            scenario_html = f'<div class="scenario"><span class="scenario_file">{scenario["location"]}</span>'
            scenario_html += f'<h3 onclick="Collapsible_toggle(\'scenario_{step_counter}\')" class="{sc_status}">'
            scenario_html += f'<span class="val">Scenario: {escape(scenario["name"])}</span></h3><ol class="scenario_steps" id="scenario_{step_counter}">'
            for step in scenario.get("steps", []):
                status = step.get("result", {}).get("status", "undefined")
                duration = step.get("result", {}).get("duration", 0.0)
                location = step.get("match", {}).get("location", "N/A")
                step_line = f'<li class="step {status}"><div class="step_name">'
                step_line += f'<span class="keyword">{step["keyword"]} </span><span class="step val">{escape(step["name"])}</span>'
                step_line += f'<small class="step_duration">({duration:.3f}s)</small></div>'
                step_line += f'<div class="step_file"><span>{location}</span></div>'
                if status == "failed":
                    error_msg = escape("\n".join(step.get("result", {}).get("error_message", [])))
                    step_line += f'<span class="embed"><a onclick="Collapsible_toggle(\'embed_{step_counter}\')">Error Message</a>'
                    step_line += f'<pre id="embed_{step_counter}" style="display: none">{error_msg}</pre></span>'
                step_line += '</li>'
                scenario_html += step_line
                step_counter += 1
            scenario_html += '</ol><span /></div>'
            html += scenario_html

    html += "</div></body></html>"

    # Write to output
    Path(output_path).write_text(html)
    print(f"✅ Report written to {output_path}")

if __name__ == "__main__":
    HTML_OUTPUT = "reports/behave_report3.html"

    run_all_features_and_collect()
    generate_behave_html_report(COMBINED_JSON, "behave-html-report.html", HTML_OUTPUT)