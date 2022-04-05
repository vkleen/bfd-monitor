{
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs;
    poetry2nix.url = github:nix-community/poetry2nix;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = inputs@{ self, nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system: let
    pkgs = import nixpkgs {
      inherit system;
      overlays = [
        inputs.poetry2nix.overlay
      ];
    };
  in rec {
    packages = {
      bfd-monitor = pkgs.poetry2nix.mkPoetryApplication {
        projectDir = ./.;
      };
      poetry = pkgs.poetry;
    };
    defaultPackage = packages.bfd-monitor;
  });
}
