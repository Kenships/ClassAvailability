import sys
import tkinter as _tk_placeholder  # noqa


def _app_py_close_to_tray_block():
    TRAY_AVAILABLE = False
    tray_holder = {}

    class A:
        def quit_app(self): pass
        def hide_window_to_tray(self): pass

    app = A()

    def close_to_tray() -> None:
        controller = tray_holder.get("controller")
        if not TRAY_AVAILABLE or controller is None:
            # No tray icon means a hidden window can't be reopened or quit, so
            # closing should exit the app rather than strand it minimized.
            app.quit_app()
            return
        controller.hide_window_to_tray()

    return close_to_tray


def _app_py_warning_block(TRAY_AVAILABLE, minimize_to_tray_on_close):
    if not TRAY_AVAILABLE and minimize_to_tray_on_close:
        try:
            print(
                "[ClassAvailability] pystray not installed; closing the window will "
                "quit the app instead of hiding to the system tray.\n"
                "Install the tray packages (`pip install -r requirements.txt`) for tray support.",
                file=sys.stderr,
            )
        except Exception:
            pass


def _gui_py_quit_button_line(ttk, btn_bar, self_obj, tk):
    ttk.Button(btn_bar, text="Quit", command=self_obj.quit_app).pack(side=tk.RIGHT)
