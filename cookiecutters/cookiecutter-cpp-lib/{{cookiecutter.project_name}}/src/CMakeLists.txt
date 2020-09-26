find_library(MATH_LIBRARY m)

add_library(${PROJECT_NAME} SHARED
  {{cookiecutter.project_name}}.cpp
  ../include/${PROJECT_NAME}/{{cookiecutter.project_name}}.hpp)

target_include_directories({{cookiecutter.project_name}} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}../include>
  $<INSTALL_INTERFACE:include>)

target_include_directories(${PROJECT_NAME} PUBLIC ../include)
if (MATH_LIBRARY)
  target_link_libraries(${PROJECT_NAME} ${MATH_LIBRARY})
endif()

install(TARGETS ${PROJECT_NAME} LIBRARY DESTINATION lib)
install(DIRECTORY ../include/${PROJECT_NAME} DESTINATION include)
