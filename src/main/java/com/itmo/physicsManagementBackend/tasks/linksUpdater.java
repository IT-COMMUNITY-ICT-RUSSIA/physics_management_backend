package com.itmo.physicsManagementBackend.tasks;

import com.itmo.physicsManagementBackend.jpa.LabWork;
import com.itmo.physicsManagementBackend.jpa.LabWorkEntry;
import com.itmo.physicsManagementBackend.jpa.LabWorkEntryRepository;
import com.itmo.physicsManagementBackend.jpa.LabWorkRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Component
public class linksUpdater {
    @Autowired
    private LabWorkEntryRepository labWorkEntryRepository;
    @Autowired
    private LabWorkRepository labWorkRepository;

    @Scheduled(fixedDelay = 30 * 1000L)
    public void updateEntries() {
        removeOld();
        addNewEntries();
    }

    private void removeOld() {
        List<LabWorkEntry> labWorkEntryList = ((List<LabWorkEntry>) labWorkEntryRepository.findAll()).stream().filter(it -> {
            return it.getStartsAt().toLocalDate().isBefore(LocalDate.now());
        }).toList();

        labWorkEntryRepository.deleteAll(labWorkEntryList);
    }

    private void addNewEntries() {
        List<LabWork> labWorkList = (List<LabWork>) labWorkRepository.findAll();
        List<LabWorkEntry> labWorkEntryList = new ArrayList<>();

        for (LabWork labWork : labWorkList) {
            for (int i = 0; i < 7; ++i) {
                LocalDate entryDate = LocalDate.now().plusDays(i);
                for (int j = 10; j <= 20; j++) {
                    labWorkEntryList.add(
                            new LabWorkEntry(
                                    UUID.fromString("%d %s".formatted(labWork.getId(), LocalDateTime.of(entryDate, LocalTime.of(j, 0)).toString())),
                                    labWork,
                                    LocalDateTime.of(entryDate, LocalTime.of(j, 0)),
                                    LocalDateTime.of(entryDate, LocalTime.of(j + 1, 0))
                            )
                    );
                }
            }
        }

        labWorkEntryRepository.saveAll(labWorkEntryList);
    }
}
