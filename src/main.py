from utils.Utils import Utils

from ui.ComprecogApplication import ComprecogApplication


def __main__():
    # выводим отладочную информацию в консоль
    Utils.print_startup_debug_info()

    app = ComprecogApplication()
    app.start()

__main__()
