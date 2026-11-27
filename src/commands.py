import subprocess


def lookup_host(hostname: str) -> str:
    # Fixture: caller-controlled text is interpolated into a shell command.
    return subprocess.check_output(["/usr/bin/nslookup", hostname], text=True)
