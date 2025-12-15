package com.greenroute.backend_core.controller;

import com.greenroute.backend_core.model.User;
import com.greenroute.backend_core.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController // Indica que esta clase responderá a peticiones HTTP devolviendo JSON
@RequestMapping("/api/users") // La "dirección" base de este controlador
@CrossOrigin(origins = "*") // Permite que Vue (puerto 9000) hable con Java (puerto 8080)
public class UserController {

    private final UserRepository userRepository;

    // Inyección de Dependencias por Constructor (Mejor práctica que @Autowired en campo)
    @Autowired
    public UserController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // GET: Obtener todos los usuarios
    // URL: http://localhost:8080/api/users
    @GetMapping
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    // POST: Crear un nuevo usuario
    // URL: http://localhost:8080/api/users
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        // En un proyecto real, aquí encriptaríamos la contraseña antes de guardar
        User savedUser = userRepository.save(user);
        return ResponseEntity.ok(savedUser);
    }
}