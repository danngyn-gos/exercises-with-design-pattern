from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_doc(self, document: str) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document: str) -> None:
        pass


class FaxDevice(ABC):
    @abstractmethod
    def fax(self, document: str) -> None:
        pass
    
    
class OldFashionedPrinter(Printer):
    def print_doc(self, document: str) -> None:
        print(f"Printing document: {document}")


class MultiFunctionDevice(Printer, Scanner, FaxDevice):
    def print_doc(self, document: str) -> None:
        print(f"MFD Printing document: {document}")

    def scan(self, document: str) -> None:
        print(f"MFD Scanning document: {document}")

    def fax(self, document: str) -> None:
        print(f"MFD Faxing document: {document}")

if __name__ == "__main__":
    # Old Fashion
    basic_printer = OldFashionedPrinter()
    basic_printer.print_doc("Document 1") 

    # Multi-function
    mfd = MultiFunctionDevice()
    mfd.print_doc("Document 4")
    mfd.scan("Document 5")
    mfd.fax("Document 6")