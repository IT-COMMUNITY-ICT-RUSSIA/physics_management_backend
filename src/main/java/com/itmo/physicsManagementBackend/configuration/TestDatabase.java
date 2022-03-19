package com.itmo.physicsManagementBackend.configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.jdbc.datasource.DriverManagerDataSource;


@Configuration
@Profile("dev")
public class TestDatabase {
    @Value("#{systemEnvironment['DB_HOST']}")
    private String dbHost;
    @Value("#{systemEnvironment['DB_NAME']}")
    private String dbName;
    @Value("#{systemEnvironment['DB_USER_NAME']}")
    private String userName;
    @Value("#{systemEnvironment['DB_PASSWORD']}")
    private String password;

    @Bean
    public DriverManagerDataSource getDataSource() {
        DriverManagerDataSource bds = new DriverManagerDataSource();
        bds.setDriverClassName("org.postgresql.Drive");
        bds.setUrl("jdbc:mysql://%s:5432/%s".formatted(dbHost, dbName));
        bds.setUsername(userName);
        bds.setPassword(password);

        return bds;
    }

}