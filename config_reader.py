import logging
import configparser
from template import Template
import pprint

logger = logging.getLogger('root')

config = configparser.ConfigParser()

config.read('template.cfg')

template_config = config['submission']

dir(template_config)
template = Template(template_config['zip_name'], template_config['folder_inside_zip'],
                    template_config['count_of_files_in_folder'], template_config['pdf_inside_zip'],
                    template_config['txt_inside_zip'])

logger.debug('Hello')
logger.debug(pprint.pformat(template.__dict__))
