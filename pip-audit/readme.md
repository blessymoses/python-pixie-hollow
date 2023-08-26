# pip-audit

pip-audit is a tool for scanning Python environments for packages with known vulnerabilities.

To audit dependencies for the current Python environment:
```bash
$ pip-audit

Found 1 known vulnerability in 1 package
Name       Version ID               Fix Versions
---------- ------- ---------------- ------------
setuptools 58.0.4  PYSEC-2022-43012 65.5.1
```

To audit dependencies for a requirements file:
```bash
$ pip-audit -r requirements.txt

No known vulnerabilities found
```

To audit dependencies for a requirements file, excluding system packages:
```bash
$ pip-audit -r requirements.txt -l

No known vulnerabilities found
```

To get the exit code:
```bash
$ pip-audit
exitcode="${?}"

Found 1 known vulnerability in 1 package
Name       Version ID               Fix Versions
---------- ------- ---------------- ------------
setuptools 58.0.4  PYSEC-2022-43012 65.5.1
$ echo $exitcode
1
```