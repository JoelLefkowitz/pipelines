const fs = require("fs");
const YAML = require("yaml");

function joinAttrs(x) {
  return Object.fromEntries(
    Object.entries(x).map((i) => [i[0], i[1].join(" ")])
  );
}

module.exports = function (grunt) {
  grunt.initConfig({
    exec: joinAttrs(YAML.parse(fs.readFileSync(".execs.yml", "utf8"))),
  });
  grunt.loadNpmTasks("grunt-exec");
  grunt.registerTask("lint", [
    "exec:pylint",
    "exec:bandit",
    "exec:cspell",
    "exec:mypy",
  ]);
  grunt.registerTask("format", [
    "exec:presort",
    "exec:black",
    "exec:autoflake",
    "exec:sort",
  ]);
  grunt.registerTask("unitTests", ["exec:pytest"]);
  grunt.registerTask("preCommit", ["lint", "format", "unitTests"]);
};
