FROM <your build env> AS build
<your build steps>

FROM <your runtime env>
COPY --from=build <your program file(s)> <location in runtime env>

ENTRYPOINT ["<command to run your app>"]