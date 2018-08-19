import json
import logging

import eel
import stix2

_log = logging.getLogger(__name__)

eel.init('ui')

class AppState():
    def __init__(self) -> None:
        self.stix_data = None

    def load_stix(self, input_string: str) -> bool:
        try:
            self.stix_data = stix2.parse(input_string)
        except (json.decoder.JSONDecodeError, stix2.exceptions.STIXError) as err:
            _log.exception(err)
            eel.set_output_text(str(err))
            return False
        eel.set_output_text(str(self.stix_data))
        return True


_state = AppState()

@eel.expose
def load_stix_string(input_string: str) -> bool:
    _log.debug('Loading string: %s', input_string)
    return _state.load_stix(input_string)

def main() -> None:
    options = {
        'mode': 'chrome-app',
        'port': 5718,
        'chromeFlags': [],
    }

    _log.info('Starting application')
    eel.start('main.html', options=options)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
