from __init__ import *

PROFILE_PICTURE = os.path.expanduser("~/.face.icon")

class User(Box):
    def __init__(self):
        super().__init__(
            name="user",
            visible=False,
            all_visible=False,
            h_expand=True,
        )
        self.user_label = Label(
            name="user-label",
            h_align="left",
            label=str(exec_shell_command('whoami')).rstrip().capitalize(),
        )
        self.host_label = Label(
            name="host-label",
            h_align="left",
            label=str(exec_shell_command('hostname')).rstrip().capitalize(),
        )
        self.user_box = Box(
            name="user-box",
            orientation="v",
            v_align="center",
            children=[
                self.user_label,
                self.host_label,
            ]
        )
        self.user_image = Box(
            name="user-image",
            style="background-image: url(\"" + PROFILE_PICTURE + "\");",
        )
        self.add(
            Box(
                name="user-container",
                h_expand=True,
                orientation="h",
                children=[
                    self.user_image,
                    self.user_box,
                ]
            )
        )