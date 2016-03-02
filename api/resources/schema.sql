drop table if exists memes;
create table memes (
  id integer primary key autoincrement,
  keywords text not null,
  filename text not null
);
