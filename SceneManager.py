from StartScene import StartScene


class SceneManager(object):
    def __init__(self):
        self.go_to(StartScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self