create table bad_ips (
    ip inet unique not null,
    status text not null check (status != ''),
    time timestamptz not null default now()
);
