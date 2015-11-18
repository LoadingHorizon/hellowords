CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(HELLO_WORDS)

SET(HELLO_WORDS_SERVER
  ./src/words_manager.cpp
  ./src/log.cpp
  ./src/hello_words_server.cpp
)

SET(HELLO_WORDS_CLIENT
  ./src/hello_words_client.cpp
)

INCLUDE_DIRECTORIES(
  "./include"
  "/usr/local/include"
)

ADD_EXECUTABLE(hello_words_server ${HELLO_WORDS_SERVER})
ADD_EXECUTABLE(hello_words_client ${HELLO_WORDS_CLIENT})

TARGET_LINK_LIBRARIES(hello_words_server
  boost_system
  ssl
  crypto
)

TARGET_LINK_LIBRARIES(hello_words_client
  boost_system
  boost_thread
  cppnetlib-client-connetctions
  cppnetlib-uri
  ssl
)

ADD_CUSTOM_TARGET(output
    mkdir bin &&
    cp hello_words_server ./bin
    cp hello_words_client ./bin
    cp ../data/words.data ./bin
)
