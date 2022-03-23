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
