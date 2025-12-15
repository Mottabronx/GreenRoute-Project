package com.greenroute.backend_core.repository;

import com.greenroute.backend_core.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Spring crea automáticamente la implementación de este método
    Optional<User> findByEmail(String email);
}