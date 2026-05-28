class TaskNotFoundException(Exception):
    def __init__(self):
        self.message = "Tarea no encontrada"