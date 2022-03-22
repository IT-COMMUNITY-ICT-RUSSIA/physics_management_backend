CREATE TABLE IF NOT EXISTS lab_work
(
    id integer primary key,
    `name` varchar (32) not null
);

CREATE TABLE IF NOT EXISTS lab_work_entry
(
    id uuid primary key,
    lab_work_id integer ,
    starts_at timestamp not null,
    completes_at timestamp not null
);

ALTER TABLE lab_work_entry
    ADD CONSTRAINT lab_work_id__fk FOREIGN KEY (lab_work_id) REFERENCES lab_work(id) ON DELETE CASCADE;