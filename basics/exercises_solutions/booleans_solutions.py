# Escribe una expresión que determine si una persona puede entrar a un club.
# La condición es que debe ser mayor o igual de 18 años.
age = 20 # (por ejemplo)
can_enter = 18 <= age
print(f"Edad: {age}, Puede entrar: {can_enter}")

# Tienes un nombre de usuario y una contraseña. El sistema solo debe permitir
# el acceso si el nombre de usuario es "admin" Y la contraseña es "provisional".
# Escribe una expresión que sea True solo si el usuario y contraseña son correctos.
username = "admin"
password = "provisional"
is_admin_login = (username == "admin") and (password == "provisional")
print(f"Usuario: '{username}', Contraseña: '{password}', Login correcto: {is_admin_login}")

# Una tienda tiene una promoción especial los sábados o los domingos.
# Escribe una expresión que determine si hoy aplica la promoción.
today = "sábado"
is_weekend_promotion = (today == "sábado") or (today == "domingo")
print(f"Hoy es {today}, Promoción activa: {is_weekend_promotion}")

# Para ver contenido premium, un usuario debe estar logueado Y NO debe tener la cuenta suspendida.
# Escribe una expresión que sea True si el usuario puede ver el contenido.
is_logged_in = True
is_account_suspended = False
can_access_premium = is_logged_in and not is_account_suspended # True AND Not(False) -> True -> Sí puede acceder
print(f"Logueado: {is_logged_in}, Suspendido: {is_account_suspended}, Puede acceder: {can_access_premium}")