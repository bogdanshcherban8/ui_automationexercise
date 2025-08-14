import allure

from components.elements.base_element import BaseElement
from tools.logger import get_logger

logger=get_logger("INPUT FILE")
class InputFile(BaseElement):
    @property
    def type_of(self)->str:
        return "input file"
    def set_input_files(self, file_path:str):
        step=f"Setting input files {self.type_of} {self.name} with file path {file_path}"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            locator.set_input_files(file_path)