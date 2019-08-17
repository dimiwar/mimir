import os
import subprocess

__app_stage = 'beta'
__app_major = '2.0.0'

__cwd = os.path.abspath(os.path.dirname(__file__))

root_path = os.path.abspath(os.path.join(__cwd, '..'))

api_keys = os.path.join(root_path, 'data/mimir.conf')
report_path = os.path.join(root_path, 'reports')

rev_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
rev_count = subprocess.check_output(["git", "rev-list", "HEAD", "--count"])

build_version = 'v{}.{}-{}_{}'.format(__app_major, rev_count.strip(), rev_hash.strip(), __app_stage)
app_version = 'v{}.{}_{}'.format(__app_major, rev_count.strip(), __app_stage)
