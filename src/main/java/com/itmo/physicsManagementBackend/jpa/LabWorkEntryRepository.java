package com.itmo.physicsManagementBackend.jpa;

import com.itmo.physicsManagementBackend.jpa.LabWorkEntry;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.repository.CrudRepository;

import java.util.UUID;

public interface LabWorkEntryRepository extends CrudRepository<LabWorkEntry, UUID> {
}
