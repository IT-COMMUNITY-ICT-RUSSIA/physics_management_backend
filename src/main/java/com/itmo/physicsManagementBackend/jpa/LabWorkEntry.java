package com.itmo.physicsManagementBackend.jpa;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.UUID;

@Getter
@Setter
@Entity
@Table(name = "lab_work_entry")
@NamedEntityGraph(name = "entry-lab-work-entity-graph",
        attributeNodes = {@NamedAttributeNode("labWork")})
@NoArgsConstructor
@AllArgsConstructor
public class LabWorkEntry {
    @Getter
    @Setter
    @Id
    @Column(nullable = false)
    UUID id;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "lab_work_id")
    LabWork labWork;
    @Column(name = "starts_at", nullable = false)
    LocalDateTime startsAt;
    @Column(name = "completes_at", nullable = false)
    LocalDateTime completesAt;

    public LabWork getLabWork() {
        return labWork;
    }
}
