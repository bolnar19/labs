Docker registry

Crea archivo de contraseñas cifradas (htpasswd) que se usa para autenticación básica (Basic Auth) en servidores web como Apache, Nginx, o en aplicaciones como un Docker registry privado.

-B: Indica que la contraseña se cifrará utilizando el algoritmo de hashing bcrypt

-c: Sobre escribe archivo "htpasswd"
registry: Nombre del usuario

```bash
$ htpasswd -Bc /auth/htpasswd registry
```
