project(CPPBackend)

set(CMAKE_CXX_STANDARD 11)

# Specify the source files
set(SOURCES
    main.cpp
    performance.cpp
    utils.cpp
)

# Add the executable
add_executable(CPPBackend ${SOURCES})