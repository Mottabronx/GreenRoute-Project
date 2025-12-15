package com.greenroute.backend_core.model;

import jakarta.persistence.*;
import lombok.Data; // Lombok genera getters/setters automágicamente
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "users") // Nombre exacto de la tabla en Postgres
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(nullable = false)
    private String passwordHash;

    // Usamos String para simplificar por ahora, luego podemos usar Enums
    private String role; 

    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    // Esto se ejecuta justo antes de guardar en la BD
    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
    }
}