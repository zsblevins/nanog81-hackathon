import subprocess
import logging
import os
import tempfile


class GNMIClient:
    def __init__(self, host, port=6030, username='admin', password='admin'):
        self.base_args = ['gnmic', '--log', '-a', f'{host}:{port}', '-u', username, '-p', password, '--insecure']
        self.logger = logging.getLogger(__name__)

    def _run(self, args):
        process = subprocess.run(args, capture_output=True)
        self.logger.debug(' '.join(process.args))
        self.logger.debug(process.stdout)
        self.logger.debug(process.stderr)
        self.logger.debug(process.returncode)
        return process.stdout

    def get(self, path):
        args = self.base_args + ['get', '--path', path]
        return self._run(args)

    def set(self, path, value):
        self.logger.debug(value)
        try:
            fname = None
            with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as fp:
                fname = fp.name
                fp.write(value.encode('utf-8'))
            args = self.base_args + ['set', '--update-path', path, '--update-file', fname]
            return self._run(args)
        finally:
            if os.path.exists(fname):
                os.remove(fname)
