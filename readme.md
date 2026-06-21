# EN
[RU](#ru)

Dependencies based on `dependency-groups'.

### Usage:
Add `dynamic_dependencies[setuptools]` to build-system.requires (in the pyproject.toml file)
```toml
[build-system]
requires = [
  "setuptools>=81.0.0",
  "dynamic_dependencies[setuptools]~=1.0",
]
```

If you use a different backend for the build:
1. Add `dynamic_dependencies` instead of `dynamic_dependencies[setuptools]`
2. Read the configuration from `pyproject.toml` `dynamic_dependencies.Config.from_pyproject`
3. Get the dependency lists by calling `dynamic_dependencies.dependencies` and `dynamic_dependencies.optional_dependencies'.
4. Write it down in the distribution information.
5. *If this is a public builder, create a PR/issue to add

### configuration:
```toml
[tool.dynamic_dependencies]
require = "name1"
optional = {
    "grp1" = "name2",
    "grp2" = "name3"
}
```

The group `name1` will be added to the required dependencies.
The group `name2` will be added to the optional dependencies as `grp1` (`...[grp1]`).
The group `name3` will be added to the optional dependencies as `grp2` (`...[grp2]`).

# RU
[EN](#en)

Зависимости основанные на `dependency-groups`.

### Использование:
Добавьте `dynamic_dependencies[setuptools]` в build-system.requires (в файл pyproject.toml)
```toml
[build-system]
requires = [
  "setuptools>=81.0.0",
  "dynamic_dependencies[setuptools]~=1.0",
]
```

Если вы используете другой бекенд для сборки:
1. Добавьте `dynamic_dependencies`, вместо `dynamic_dependencies[setuptools]`
2. Прочтите конфигурацию из `pyproject.toml` `dynamic_dependencies.Config.from_pyproject`
3. Получите списки зависимостей вызвав `dynamic_dependencies.dependencies` и `dynamic_dependencies.optional_dependencies`.
4. Запишите в информацию о дистрибутиве.
5. *Если это публичный сборщик, создайте PR/issue на добавление

### конфигурация:

```toml
[tool.dynamic_dependencies]
require = "name1"
optional = {
    "grp1" = "name2",
    "grp2" = "name3"
}
```

Группа `name1` будет добавлена в обязательные зависимости.
Группа `name2` будет добавлена в НЕобязательные зависимости как `grp1` (`...[grp1]`).
Группа `name3` будет добавлена в НЕобязательные зависимости как `grp2` (`...[grp2]`).
