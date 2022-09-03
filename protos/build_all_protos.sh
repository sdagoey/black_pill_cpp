#!/bin/bash
cd ../EmbeddedProto
protoc --plugin=protoc-gen-eams=protoc-gen-eams -I../protos --eams_out=../Core/Generated ../protos/basic_control.proto

