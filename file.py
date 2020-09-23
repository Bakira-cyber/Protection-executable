from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

# security
licence_workbook = load_workbook("database-Licence.xlsx", read_only=False, keep_vba=True)
licence_workbook.security = WorkbookProtection(workbookPassword='TzeentchFavoriteNumberis9!',
                                               revisionsPassword='TzeentchFavoriteNumberis9', lockWindows=True,
                                               lockStructure=True, lockRevision=True)
licence_workbook.save("database-Licence.xlsx")
licence_workbook.close()
