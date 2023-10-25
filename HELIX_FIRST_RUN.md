# Helix Flatpak

You are running flatpak version of Helix. This version is running inside
of a container and is therefore not able to access tools on your host
system.

You can open issues related to this flatpak at
https://github.com/flathub/com.helix_editor.Helix/issues

## Running Commands on the Host System

To run commands on the host system from inside of the sandbox, you
can use flatpak-spawn:

```sh
flatpak-spawn --host <COMMAND>
```

## Adding Language Servers Installed on the Host

If you want to use a language server installed on your host system, you
will need to edit `languages.toml` file. For example:

```toml
# ~/.var/app/com.helix_editor.Helix/config/helix/languages.toml

[language-server.rust-analyzer-host]
command = "flatpak-spawn"
args = ["--host", "rust-analyzer"]

[[language]]
name = "rust"
language-servers = [
  { name = "rust-analyzer-host" }
]
```

This will allow you to use rust-analyzer installed on your host
system from within the Flatpak container. For full documentation on
how to configure language servers, see
https://docs.helix-editor.com/languages.html

## Installing Flatpak SDK Extensions

By default, this flatpak has access to standard development environment
provided by `org.freedesktop.Sdk` with programs such as GCC and Python.
However, if you need support for additional languages (including
language servers), you will need to install SDK extensions. For example:

```sh
flatpak install flathub org.freedesktop.Sdk.Extension.rust-stable
flatpak install flathub org.freedesktop.Sdk.Extension.llvm16
```

This will install the Rust and LLVM SDK extensions. After this you will
have your extensions at `/usr/lib/sdk/<extension-name>`. But they won't
be added to `$PATH`.

## Enabling SDK Extensions

To enable SDK extensions you will need to set `FLATPAK_ENABLE_SDK_EXT`
environment variable to a comma-separated list of extension names.
For example:

```sh
FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm16 flatpak run com.helix_editor.Helix
```

This will add compilers, language servers, debug adapters, and other
tools to your `$PATH`.

## Checking Language Server Detection

To check which language servers have been detected, run Helix with the
`--health` option:

```sh
FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm16 flatpak run com.helix_editor.Helix --health
```

You can also get information about a specific language:

```sh
FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm16 flatpak run com.helix_editor.Helix --health rust
```

## Making Changes Persistent

To set environment variables persistently, use `flatpak override`:

```sh
flatpak override --user com.helix_editor.Helix --env=FLATPAK_ENABLE_SDK_EXT="rust-stable,llvm16"
```

## Finding Other SDK Extensions

To find other SDK extensions, use `flatpak search`:

```sh
flatpak search <TEXT>
```