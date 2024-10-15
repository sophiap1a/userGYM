import pygame
import time
import user_service


pygame.init()  # Inicializar Pygame
clock = pygame.time.Clock()
timer_start = time.time()
WIDTH = 500
HEIGHT = 800

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GYM")

# Cargar y escalar las imágenes de fondo para la pantalla del menú de una sola vez 
background_images_menu = [
    pygame.transform.scale(pygame.image.load("assets//img//back1.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("assets//img//princi1.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("assets//img//princi2.png").convert(), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load("assets//img//princi3.png").convert(), (WIDTH, HEIGHT)),
]

# Fondo para pantalla de registro 
background_image_register = pygame.transform.scale(pygame.image.load("assets/users/users_1.png").convert(), (WIDTH, HEIGHT))
background_image_create = pygame.transform.scale(pygame.image.load("assets/users/create.png").convert(), (WIDTH, HEIGHT))
background_image_edit = pygame.transform.scale(pygame.image.load("assets/users/edit.png").convert(), (WIDTH, HEIGHT))
input_boxes = [pygame.Rect(150, 200 + i*60, 200, 32) for i in range(2)] 
button_edit_user = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 300, 200, 40)
button_create_user = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2 + 300, 180, 40)
create_input_boxes = [pygame.Rect(150, 470 + i * 100, 300, 52) for i in range(2)]
create_input_texts = [''] * 2  
create_active_box = -1
edit_input_boxes = [pygame.Rect(140, 310 + i * 125, 300, 42) for i in range(4)]
edit_input_texts = [''] * 4  
edit_active_box = -1
back_button_rect = pygame.Rect(20, 20, 40, 40) 

# Cargar y escalar la imágen de fondo para la tercerapantalla (género)
background_image_gender = pygame.transform.scale(pygame.image.load("assets/screen2/screen1.png").convert(), (WIDTH, HEIGHT))

# Cargar y escalar la imagen de fondo 3
background_image_man = pygame.transform.scale(pygame.image.load("assets/gender/man.png").convert(), (WIDTH, HEIGHT))
background_image_women = pygame.transform.scale(pygame.image.load("assets/gender/women.png").convert(), (WIDTH, HEIGHT))

current_image_index = 0  # Índice de la imagen actual para el menú
animation_time = 0.3  # Tiempo entre imágenes en segundos
last_update_time = time.time()  # Última actualización de la imagen

# Definir el botón invisible 
button_start = pygame.Rect(WIDTH - 300 - 98, HEIGHT - 120, 375, 68)

# boton gender # Ajustar la posición y el tamaño del botón masculino
button_mf_width = 450  # Nuevo ancho del botón
button_mf_height = 140  # Altura del botón
button_male_x = (WIDTH - button_mf_width) // 2  # Centrado horizontalmente
button_male = pygame.Rect(button_male_x, HEIGHT - 560, button_mf_width, button_mf_height)  # Botón masculino
button_female_x = (WIDTH - button_mf_width) // 2  # Centrado horizontalmente
button_female = pygame.Rect(button_male_x, HEIGHT - 320, button_mf_width, button_mf_height)

# Pantalla de los ejercicios 
background_image_rutine_men = pygame.transform.scale(pygame.image.load("assets//rutine//rutine_exer_man.png").convert(), (WIDTH, HEIGHT))
background_image_rutine_women = pygame.transform.scale(pygame.image.load("assets/rutine/background_eje.png").convert(), (WIDTH, HEIGHT))
button_width = 200
button_height = 51

buttons_rutine = [
    pygame.Rect((WIDTH - button_width) // 2, 180, button_width, button_height),  # Botón para ejercicio 1
    pygame.Rect((WIDTH - button_width) // 2, 243, button_width, button_height),  # Botón para ejercicio 2
    pygame.Rect((WIDTH - button_width) // 2, 306, button_width, button_height),  # Botón para ejercicio 3
    pygame.Rect((WIDTH - button_width) // 2, 365, button_width, button_height),  # Botón para ejercicio 4
    pygame.Rect((WIDTH - button_width) // 2, 429, button_width, button_height)   # Botón para ejercicio 5
]

# Cargar animaciones para los ejercicios (puedes cargar imágenes específicas para cada ejercicio)

exercise_animations = {
    "Flexiones": [
        pygame.image.load("assets/rutine/exer_man/tijera1.png"),
        pygame.image.load("assets/rutine/exer_man/tijera2.png")
    ],
    "Fondos en silla": [
        pygame.image.load("assets/rutine/2/Screenshot 2024-09-29 123507.png"),
        pygame.image.load("assets/rutine/2/Screenshot 2024-09-29 123512.png")
    ],
    "Press de pecho con mancuernas": [
        pygame.image.load("assets/rutine/18/Screenshot 2024-09-29 133202.png"),
        pygame.image.load("assets/rutine/18/Screenshot 2024-09-29 133207.png")
    ],
    "Aperturas con mancuernas": [
        pygame.image.load("assets/rutine/6/Screenshot 2024-09-29 133607.png"),
        pygame.image.load("assets/rutine/6/Screenshot 2024-09-29 133612.png")
    ],
    "Extensiones de tríceps": [
        pygame.image.load("assets/rutine/16/Screenshot 2024-09-29 133211.png"),
        pygame.image.load("assets/rutine/16/Screenshot 2024-09-29 133215.png")
    ],
    "Remo con mancuernas": [
        pygame.image.load("assets/rutine/Screenshot 2024-09-29 133230.png")  # 
    ],
    "Pull-ups": [
        pygame.image.load("assets/rutine/5/Screenshot 2024-09-29 133617.png"),
        pygame.image.load("assets/rutine/5/Screenshot 2024-09-29 133622.png")
    ],
    "Curl de bíceps": [
        pygame.image.load("assets/rutine/13/Screenshot 2024-09-29 133236.png"),
        pygame.image.load("assets/rutine/13/Screenshot 2024-09-29 133239.png")
    ],
    "Remo invertido": [
        pygame.image.load("assets/rutine/4/Screenshot 2024-09-29 133628.png")
    ],
    "Curl martillo": [
        pygame.image.load("assets/rutine/8/Screenshot 2024-09-29 133536.png"),
        pygame.image.load("assets/rutine/8/Screenshot 2024-09-29 133504.png")
    ],
    "Sentadillas": [
        pygame.image.load("assets/rutine/Screenshot 2024-09-29 133255.png")#
    ],
    "Zancadas": [
        pygame.image.load("assets/rutine/10/Screenshot 2024-09-29 133429.png"),
        pygame.image.load("assets/rutine/10/Screenshot 2024-09-29 133444.png")
    ],
    "Puente de glúteos": [
        pygame.image.load("assets/rutine/11/Screenshot 2024-09-29 133335.png"),
        pygame.image.load("assets/rutine/11/Screenshot 2024-09-29 133338.png")
    ],
    "Elevaciones de talones": [
        pygame.image.load("assets/rutine/12/Screenshot 2024-09-29 133310.png"),
        pygame.image.load("assets/rutine/12/Screenshot 2024-09-29 133314.png")
    ],
    "Sentadillas con salto": [
        pygame.image.load("assets/rutine/19/Screenshot 2024-09-29 133319.png"),#
        pygame.image.load("assets/rutine/19/Screenshot 2024-09-29 133322.png")
    ],
    "Press militar": [
        pygame.image.load("assets/rutine/Screenshot 2024-09-29 133330.png") #
    ],
    "Elevaciones laterales": [
        pygame.image.load("assets/rutine/11/Screenshot 2024-09-29 133335.png"),
        pygame.image.load("assets/rutine/11/Screenshot 2024-09-29 133338.png")
    ],
    "Elevaciones frontales": [
        pygame.image.load("assets/rutine/17/Screenshot 2024-09-29 133346.png"),
        pygame.image.load("assets/rutine/17/Screenshot 2024-09-29 133346.png")
    ],
    "Encogimientos de hombros": [
        pygame.image.load("assets/rutine/18/Screenshot 2024-09-29 133202.png"),
        pygame.image.load("assets/rutine/18/Screenshot 2024-09-29 133207.png")
    ],
    "Remo al mentón": [
        pygame.image.load("assets/rutine/Screenshot 2024-09-29 133407.png")  # 
    ],
    "Plancha": [
        pygame.image.load("assets/rutine/Screenshot 2024-09-29 133412.png") 
    ],
    "Abdominales bicicleta": [
        pygame.image.load("assets/rutine/10/Screenshot 2024-09-29 133429.png"),
        pygame.image.load("assets/rutine/10/Screenshot 2024-09-29 133444.png")  # Cambia esta ruta si es necesario
    ],
    "Elevaciones de piernas": [
        pygame.image.load("assets/rutine/9/Screenshot 2024-09-29 133450.png"),
        pygame.image.load("assets/rutine/9/Screenshot 2024-09-29 133454.png")  # Cambia esta ruta si es necesario
    ],
    "Mountain climbers": [
        pygame.image.load("assets/rutine/8/Screenshot 2024-09-29 133504.png"),
        pygame.image.load("assets/rutine/8/Screenshot 2024-09-29 133536.png")  # Cambia esta ruta si es necesario
    ],
    "Burpees": [
        pygame.image.load("assets/rutine/7/Screenshot 2024-09-29 133550.png"),
        pygame.image.load("assets/rutine/7/Screenshot 2024-09-29 133555.png"),
        pygame.image.load("assets/rutine/7/Screenshot 2024-09-29 133602.png"),
    ],
}
# Definir las rutinas con series y repeticiones
rutinas = {
    "Pecho y Tríceps": [
        {"ejercicio": "Flexiones", "series": 3, "reps": 12, "tiempo": 0},
        {"ejercicio": "Fondos en silla", "series": 3, "reps": 10, "tiempo": 0},
        {"ejercicio": "Press de pecho con mancuernas", "series": 3, "reps": 12,"tiempo": 0},
        {"ejercicio": "Aperturas con mancuernas", "series": 3, "reps": 12,"tiempo": 0},
        {"ejercicio": "Extensiones de tríceps", "series": 3, "reps": 12, "tiempo": 0}
    ],
    "Espalda y Bíceps": [
        {"ejercicio": "Remo con mancuernas", "series": 3, "reps": 12, "tiempo": 0},
        {"ejercicio": "Pull-ups", "series": 3, "reps": 8, "tiempo": 0},
        {"ejercicio": "Curl de bíceps", "series": 3, "reps": 12, "tiempo": 0},
        {"ejercicio": "Remo invertido", "series": 3, "reps": 10, "tiempo": 0},
        {"ejercicio": "Curl martillo", "series": 3, "reps": 12, "tiempo": 0}
    ],
    "Piernas": [
        {"ejercicio": "Sentadillas", "series": 3, "reps": 15, "tiempo": 0},
        {"ejercicio": "Zancadas", "series": 3, "reps": 12, "tiempo": 0},
        {"ejercicio": "Puente de glúteos", "series": 3, "reps": 15, "tiempo": 0},
        {"ejercicio": "Elevaciones de talones", "series": 3, "reps": 20, "tiempo": 0},
        {"ejercicio": "Sentadillas con salto", "series": 3, "reps": 12, "tiempo": 0}
    ],
    "Hombros y Trapecio": [
        {"ejercicio": "Press militar", "series": 3, "reps": 12, "tiempo": 10},
        {"ejercicio": "Elevaciones laterales", "series": 3, "reps": 12, "tiempo": 10},
        {"ejercicio": "Elevaciones frontales", "series": 3, "reps": 12, "tiempo": 10},
        {"ejercicio": "Encogimientos de hombros", "series": 3, "reps": 15, "tiempo": 10},
        {"ejercicio": "Remo al mentón", "series": 3, "reps": 12, "tiempo": 10}
    ],
    "Core y Cardio": [
        {"ejercicio": "Plancha", "series": 3, "reps": 1, "tiempo": 60},  # 1 minuto por serie
        {"ejercicio": "Abdominales bicicleta", "series": 3, "reps": 15, "tiempo": 0},
        {"ejercicio": "Elevaciones de piernas", "series": 3, "reps": 15, "tiempo": 0},
        {"ejercicio": "Mountain climbers", "series": 3, "reps": 30, "tiempo": 30},  # 30 segundos por serie
        {"ejercicio": "Burpees", "series": 3, "reps": 10, "tiempo": 0}
    ]
}# Control de estado
current_rutina = "Pecho y Tríceps"
current_exercise_index = 0
current_series = 1
current_reps = rutinas[current_rutina][current_exercise_index]["reps"]
animation_frame = 0
last_update_time = time.time()
 
points = 0
paused = False

# Botones
button_done = pygame.Rect(WIDTH - 150, HEIGHT - 100, 130, 50)
button_pause = pygame.Rect(WIDTH - 300, HEIGHT - 100, 120, 50)
button_resume = pygame.Rect(WIDTH - 450, HEIGHT - 100, 120, 50)
button_back = pygame.Rect(WIDTH - 495, 10, 50, 50)
button_back_to_menu = pygame.Rect(WIDTH // 2 - 80, HEIGHT - 100, 200, 50)

# Estado inicial (pantalla de menú)
current_state = "menu"
select_gender = None  # Como no hay nada seleccionado almacena nada 
rutine = None 
show_next_message = False
# Para registro
input_box_width = 300
input_box_height = 50
input_box_y_start = 300  # Starting Y position for the first input box
input_boxes = [pygame.Rect((WIDTH - input_box_width) // 2, input_box_y_start + i * (input_box_height + 10), input_box_width, input_box_height) for i in range(2)]
active_box = -1
current_user = None
register_mode = False
input_texts = [''] * 2
error_message = None
select_action_user = None
error_message_2 = None
error_message_edit = None
# Función del menú
def menu():
    global current_image_index, last_update_time, current_state # Añadir variables globales
    
    # Comprobar si es tiempo de cambiar la imagen del fondo
    if time.time() - last_update_time > animation_time:
        current_image_index = (current_image_index + 1) % len(background_images_menu)
        last_update_time = time.time()  # Reiniciar el temporizador

    # Dibujar la imagen del fondo actual en la pantalla
    window.blit(background_images_menu[current_image_index], (0, 0))
    

def register():
    global input_texts, active_box, current_state, current_user, register_mode
    
    window.blit(background_image_register, (0,0))

    font = pygame.font.Font(None, 36)
# Definir nuevas posiciones para las cajas de entrada
    input_box_x_start = 140
    input_box_y_start = 550  # Nueva posición para las cajas
    spacing = 92  # Espacio entre las cajas

    # Dibujar cuadros de entrada
    for i, box in enumerate(input_boxes):
        box.x = input_box_x_start 
        box.y = input_box_y_start + i * spacing  # Actualizar la posición de la caja
        pygame.draw.rect(window, (255, 255, 255), box, 2)  # Dibujar el borde de la caja
        text_surface = font.render(input_texts[i], True, (0, 0, 0))
        window.blit(text_surface, (box.x + 5, box.y + 5))  # Dibujar texto dentro de la caja

    # Handle focus for the active input box
    if active_box != -1:
        pygame.draw.rect(window, (0, 255, 0), input_boxes[active_box], 2)  # Highlight active box
        
    if error_message:
        error_font = pygame.font.Font(None, 24)
        error_surface = error_font.render(error_message, True, (0, 0, 0))
        window.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, HEIGHT // 2 + 300))
    
def show_action_user_screen():
    global select_action_user

    if select_action_user == "create":
        window.blit(background_image_create, (0, 0))  # Mostrar imagen de hombre
    elif select_action_user == "edit":
        window.blit(background_image_edit, (0, 0))  # Mostrar imagen de mujer
        
def handle_create_input():
    global create_active_box

    font = pygame.font.Font(None, 36)

    # Dibujar cuadros de entrada
    for i, box in enumerate(create_input_boxes):
        pygame.draw.rect(window, (255, 255, 255), box, 2)  # Dibujar el borde de la caja
        text_surface = font.render(create_input_texts[i], True, (0, 0, 0))
        window.blit(text_surface, (box.x + 5, box.y + 5))  # Dibujar texto dentro de la caja

        # Manejar foco para la caja activa
        if create_active_box == i:
            pygame.draw.rect(window, (0, 255, 0), box, 2)  # Resaltar la caja activa
    
    if error_message_2:
        error_font = pygame.font.Font(None, 24)
        error_surface = error_font.render(error_message_2, True, (0, 0, 0))  
        window.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, HEIGHT // 2 + 300))
        
        pygame.draw.rect(window, (255, 0, 0), back_button_rect)    
        
def handle_edit_input():
    global edit_active_box

    font = pygame.font.Font(None, 36)

    # Dibujar cuadros de entrada
    for i, box in enumerate(edit_input_boxes):
        pygame.draw.rect(window, (255, 255, 255), box, 2)  # Dibujar el borde de la caja
        text_surface = font.render(edit_input_texts[i], True, (0, 0, 0))
        window.blit(text_surface, (box.x + 5, box.y + 5))  # Dibujar texto dentro de la caja

        # Manejar foco para la caja activa
        if edit_active_box == i:
            pygame.draw.rect(window, (0, 255, 0), box, 2)  # Resaltar la caja activa
    
    if error_message_edit:
        error_font = pygame.font.Font(None, 24)
        error_surface = error_font.render(error_message_edit, True, (0, 0, 0))  # Texto rojo para el error
        window.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, HEIGHT // 2 + 330))
    
def gender():
    # Dibujar la imagen de fondo para la pantalla "género"
    window.blit(background_image_gender, (0, 0))
    
def show_gender_screen():
    global select_gender

    if select_gender == "male":
        window.blit(background_image_man, (0, 0))  # Mostrar imagen de hombre
    elif select_gender == "female":
        window.blit(background_image_women, (0, 0))  # Mostrar imagen de mujer
        
    font = pygame.font.Font(None, 36)
    points_surface = font.render(f"Puntos: {points}", True, (255, 255, 255))
    window.blit(points_surface, (5, 760))  # Mostrar en la esquina superior izquierda

def rutine_screen():
    global remaining_time, paused, points, timer_start, show_next_message

    # Cambiar el fondo de rutina según el género seleccionado
    if select_gender == "male":
        window.blit(background_image_rutine_men, (0, 0))
    elif select_gender == "female":
        window.blit(background_image_rutine_women, (0, 0))

    font = pygame.font.Font(None, 36)

    # Mostrar el nombre del ejercicio actual
    if current_exercise_index < len(rutinas[current_rutina]):
        current_exercise = rutinas[current_rutina][current_exercise_index]
        current_exercise_name = current_exercise["ejercicio"]
        series_reps_text = f"Series: {current_exercise['series']}    x    Reps: {current_exercise['reps']}"
        series_reps_surface = font.render(series_reps_text, True, (0, 0, 0))
        window.blit(series_reps_surface, (WIDTH // 2 - series_reps_surface.get_width() // 2, HEIGHT // 2 + 70))

        exercise_time = current_exercise["tiempo"]

        # Mostrar el cronómetro solo si es necesario y no está pausado
        if exercise_time > 0 and not paused:
            if timer_start == 0:
                timer_start = time.time()
            elapsed_time = time.time() - timer_start
            remaining_time = max(0, exercise_time - elapsed_time)
            timer_text = f"Tiempo: {int(remaining_time)}s "
            text_surface = font.render(timer_text, True, (0, 0, 0))
            time_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
            window.blit(text_surface, time_rect)

            if remaining_time <= 0:
                next_exercise()
                show_next_message = True  # Mostrar el mensaje cuando se termine la serie
        elif exercise_time == 0:
            timer_start = 0  # Reiniciar el temporizador si no se necesita

        # Dibujar el nombre del ejercicio
        exercise_name_surface = font.render(current_exercise_name, True, (0, 0, 0))
        text_width = exercise_name_surface.get_width()
        centered_x = 250 - text_width // 2
        window.blit(exercise_name_surface, (centered_x, 410))

    else: 
        show_final_score()
        current_state = "final_score"

    # Mostrar mensaje para seguir
    font_size_1 = 25
    font = pygame.font.Font(None, font_size_1)
    if show_next_message:
        next_message_surface = font.render("Dale click a Siguiente cada que acabes una serie", True, (0, 0, 0))
        window.blit(next_message_surface, (WIDTH // 2 - next_message_surface.get_width() // 2, HEIGHT - 150))

    # Dibujar botones
    font_size = 34
    font = pygame.font.Font(None, font_size)
    pygame.draw.rect(window, (255, 255, 255), button_done)
    pygame.draw.rect(window, (255, 255, 255), button_pause)
    pygame.draw.rect(window, (255, 255, 255), button_back)

    # Texto de los botones
    window.blit(font.render("Siguiente", True, (0, 0, 0)), (button_done.x + 10, button_done.y + 10))
    window.blit(font.render("Pausa", True, (0, 0, 0)), (button_pause.x + 10, button_pause.y + 10))
    if paused:
        window.blit(font.render("Continuar", True, (0, 0, 0)), (button_resume.x + 10, button_resume.y + 10))
    window.blit(font.render("<", True, (0, 0, 0)), (button_back.x + 10, button_back.y + 10))
def draw_current_exercise():
    global animation_frame, last_update_time

    if current_exercise_index < len(rutinas[current_rutina]):
        ejercicio_actual = rutinas[current_rutina][current_exercise_index]["ejercicio"]

        if time.time() - last_update_time > 0.5:  # Control de velocidad de la animación
            animation_frame = (animation_frame + 1) % len(exercise_animations[ejercicio_actual])
            last_update_time = time.time()

        # Dibujar el frame de la animación
        animation_image = pygame.transform.scale(exercise_animations[ejercicio_actual][animation_frame], (300, 300))
        window.blit(animation_image, (WIDTH // 4 - 25, 100))  # Centrar en la pantalla

# En el bucle principal
if current_state == "rutine":
    rutine_screen()  # Mostrar la pantalla de rutina
    draw_current_exercise()  # Dibujar la animación del ejercicio actual

    
# Función para avanzar al siguiente ejercicio
def next_exercise():
    global current_exercise_index, current_series, timer_start
    if current_series < rutinas[current_rutina][current_exercise_index]["series"]:
        current_series += 1  # Avanza a la siguiente serie
    else:
        current_series = 1  # Reiniciar series para el siguiente ejercicio
        current_exercise_index += 1  # Avanza al siguiente ejercicio
    timer_start = 0
def show_final_score():
    window.fill((0, 0, 0))  # Pantalla negra
    font = pygame.font.Font(None, 36)
    score_text = f"Puntos totales: {points}"
    text_surface = font.render(score_text, True, (255, 255, 255))
    window.blit(text_surface, (WIDTH // 2 - 100, HEIGHT // 2))

    # Botón para volver al menú
    pygame.draw.rect(window, (255, 255, 255), button_back_to_menu)
    window.blit(font.render("Volver al menú", True, (0, 0, 0)), (button_back_to_menu.x + 10, button_back_to_menu.y + 10))

# Bucle principal
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Salir del bucle si se cierra la ventana

        # Detectar clic del mouse en el estado del menú
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "menu":
            mouse_pos = event.pos  # Obtener la posición del clic
            if button_start.collidepoint(mouse_pos):
                current_state = "register"  # Cambiar al estado siguiente cuando se presiona el botón+
                
                        # Detectar clic del mouse en la pantalla de registro
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "register":
            mouse_pos = event.pos  # Obtener la posición del clic
            
        # Detectar clic del mouse en la pantalla de registro
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "register":
            mouse_pos = event.pos  # Obtener la posición del clic
            
            # Detectar clic en el botón Editar
            if button_edit_user.collidepoint(mouse_pos):
                select_action_user = "edit"
                current_state = "show_action_user"  # Cambiar de estado para mostrar la pantalla de edición de usuario
            
            # Detectar clic en el botón Crear
            elif button_create_user.collidepoint(mouse_pos):
                select_action_user = "create"
                current_state = "show_action_user"  # Cambiar de estado para mostrar la pantalla de creación de usuario

        # Manejar la pantalla de acción del usuario (crear o editar)
        if current_state == "show_action_user":
            show_action_user_screen()
    
    
        if event.type == pygame.KEYDOWN:
            if active_box != -1:  
                if event.key == pygame.K_RETURN:  
                    active_box = (active_box + 1) % len(input_boxes) 
                elif event.key == pygame.K_BACKSPACE:
                    input_texts[active_box] = input_texts[active_box][:-1]  
                else:
                    input_texts[active_box] += event.unicode  

    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, box in enumerate(input_boxes):
                if box.collidepoint(mouse_pos):
                    active_box = i  
                    
        if event.type == pygame.KEYDOWN:
            if active_box != -1:
                if event.key == pygame.K_RETURN:
                    # Verificar usuario y contraseña
                    username = input_texts[0]
                    password = input_texts[1]
                    if user_service.check_credentials(username, password):  # Verifica las credenciales
                        current_state = "gender"  # Cambiar al estado de género
                        error_message = None  # Limpiar el mensaje de error
                    else:
                        error_message = "Usuario o contraseña incorrectos"
                        
        if event.type == pygame.KEYDOWN:
            if select_action_user == "create" and create_active_box != -1:  # Solo capturar si la caja está activa
                if event.key == pygame.K_RETURN:  # Al presionar Enter, cambiar el foco
                    create_active_box = (create_active_box + 1) % len(create_input_boxes)  # Ciclar entre las cajas
                elif event.key == pygame.K_BACKSPACE:
                    create_input_texts[create_active_box] = create_input_texts[create_active_box][:-1]  # Eliminar el último carácter
                else:
                    create_input_texts[create_active_box] += event.unicode  # Añadir el carácter ingresado

        # Comprobar clic del mouse para establecer la caja activa
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, box in enumerate(create_input_boxes):
                if box.collidepoint(mouse_pos):
                    create_active_box = i  # Establecer la caja activa en la que se hizo cli            
                        
        # Al presionar Enter en la última caja de entrada
        if create_active_box == len(create_input_boxes) - 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
    # Intenta crear el usuario solo si se encuentra en la última caja de entrada
            username = create_input_texts[0] if len(create_input_texts) > 0 else ""  # Asegúrate de que username esté definido
            password = create_input_texts[1] if len(create_input_texts) > 1 else ""  # Asegúrate de que password esté definido

            try:
        # Intenta crear el usuario
                user_service.create_user(username, password=password)  # Llama a create_user

        # Si la creación es exitosa, cambia el estado
                error_messag_2 = None  # Limpia el mensaje de error
                current_state = "gender"  # Cambia al estado de género
                reate_input_texts = [''] * len(create_input_boxes)  # Reinicia las entradas

            except Exception as e:
        # Manejo de errores
                error_message_2 = str(e)  # Guarda el mensaje de error
          
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if back_button_rect.collidepoint(mouse_pos):
                current_state = "register"  # Cambiar al estado anterior
  

         
        if select_action_user == "edit":
            if event.type == pygame.KEYDOWN:
                if edit_active_box != -1:  # Solo capturar si la caja está activa
                    if event.key == pygame.K_RETURN:
                        edit_active_box = (edit_active_box + 1) % len(edit_input_boxes)  # Cambiar el foco
                    elif event.key == pygame.K_BACKSPACE:
                        edit_input_texts[edit_active_box] = edit_input_texts[edit_active_box][:-1]  # Eliminar el último carácter
                    else:
                        edit_input_texts[edit_active_box] += event.unicode  # Añadir el carácter ingresado

                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, box in enumerate(edit_input_boxes):
                if box.collidepoint(mouse_pos):
                    edit_active_box = i  # Establecer la caja activa en la que se hizo clic  
                    
                    
                           
        if event.type == pygame.KEYDOWN:
            if edit_active_box != -1:  # Solo capturar si la caja está activa
                if event.key == pygame.K_RETURN:
                    if edit_active_box == len(edit_input_boxes) - 1:  # Solo en la última caja
                        username = edit_input_texts[0] if len(edit_input_texts) > 0 else ""
                        password = edit_input_texts[1] if len(edit_input_texts) > 1 else ""
                        new_username = edit_input_texts[2]  # Nuevo usuario
                        new_password = edit_input_texts[3]  # Nueva contraseña

                        # Asegúrate de que todos los campos estén presentes
                        if username and password and new_username and new_password:
                            try:
                                # Intenta actualizar el usuario, incluyendo la nueva contraseña
                                user_service.update_user(username, password=new_password, new_username=new_username)
                                success_message = f"Usuario {new_username} actualizado con éxito!"
                                error_message_edit = None
                                current_state = "gender"
                                edit_input_texts = [''] * len(edit_input_boxes)
                                edit_active_box = -1  # Restablecer el foco
                            except Exception as e:
                                error_message_edit = str(e)
                                
                        else:
                            error_message_edit = "Por favor, complete todos los campos."
   
      
        # Detectar clic del mouse en la pantalla de "género"
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "gender":
            mouse_pos = event.pos  # Obtener la posición del clic
            if button_male.collidepoint(mouse_pos):
                select_gender = "female"  
                current_state = "show_gender"
            elif button_female.collidepoint(mouse_pos):
                select_gender = "male"  
                current_state = "show_gender"


        # Detectar clic del mouse en la pantalla de género para los ejercicios
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "show_gender":
            mouse_pos = event.pos
            for i, button in enumerate(buttons_rutine):
                if button.collidepoint(mouse_pos):
                    current_rutina = list(rutinas.keys())[i]  # Asignar el nombre de la rutina seleccionada
                    current_exercise_index = 0  # Reiniciar el índice de ejercicio
                    current_series = 1  # Reiniciar las series
                    timer_start = time.time()  # Reiniciar el temporizador
                    current_state = "rutine"        
       # Detectar clic del mouse para avanzar en los ejercicios
        if event.type == pygame.MOUSEBUTTONDOWN and current_state == "rutine":
            mouse_pos = event.pos
            if button_done.collidepoint(mouse_pos):
                points += 10
                next_exercise()
                show_next_message = True
            elif button_pause.collidepoint(mouse_pos):
                paused = True
                timer_start = time.time()
            elif button_back.collidepoint(mouse_pos):
                # Lógica para retroceder
                if current_exercise_index > 0:
                    current_exercise_index -= 1
                    current_series = 1  # Reiniciar series si retrocede
                else:
                    current_state = "gender"
                timer_start = 0
                    
        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_resume.collidepoint(mouse_pos):
                paused = False  # Continuar

        # Detectar clic del mouse en la pantalla de puntuación final
    if event.type == pygame.MOUSEBUTTONDOWN and current_state == "final_score":
        mouse_pos = event.pos
        if button_back_to_menu.collidepoint(mouse_pos):
            current_state = "gender"  # Volver al menú
            current_exercise_index = 0  # Reiniciar el índice de ejercicio
                
    # Ejecutar la lógica de la pantalla actual
    if current_state == "menu":
        menu()  # Mostrar la pantalla del menú
    if current_state == "register":
        register()
    elif current_state == "show_action_user":
        show_action_user_screen()
        if select_action_user == "create":
            handle_create_input()
        if select_action_user == "edit":
            handle_edit_input()
    elif current_state == "gender":
        gender()  # Mostrar la pantalla de "género"
    elif current_state == "show_gender":
        show_gender_screen()  # Mostrar la pantalla de "hombre" o "mujer"
    elif current_state == "rutine":
        rutine_screen()  # Mostrar la pantalla de rutina
        draw_current_exercise()  # Draw the current exercise animation
            
    if current_exercise_index >= len(rutinas[current_rutina]):
        show_final_score()
        current_state = "final_score"  # Volver al menú o reiniciar
        
    pygame.display.update()  # Actualizar la pantalla
    clock.tick(30)