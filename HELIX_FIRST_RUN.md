
# Running Helix Flatpak Version

If you are running the Flatpak version of Helix, you may encounter some limitations due to the fact that it runs inside a container and cannot access tools on your host system. However, there are some workarounds that you can use to execute commands on the host system and get support for additional languages.

## Opening Issues

If you encounter any issues related to the Flatpak version of Helix, you can open them at https://github.com/flathub/@FLATPAK_ID@/issues.

## Executing Commands on the Host System

To execute commands on the host system, you can use the following command:

```sh
$ flatpak-spawn --host <COMMAND>
```

This will allow you to execute commands on the host system from within the Flatpak container.

## Adding Language Server Entries

If you want to use a language server installed on your host system, you will need to add an entry to your `languages.toml` file. For example:

```toml
[[language]]
name = "rust"
language-server = { command = "flatpak-spawn", args = ["--host", "rust-analyzer"] }
```

This will allow you to use the Rust language server installed on your host system from within the Flatpak container.

## Installing Flatpak SDK Extensions

By default, the Flatpak version of Helix provides access to standard development environments such as GCC and Python. However, if you need support for additional languages (including language servers), you will need to install SDK extensions.

To install SDK extensions, use the following commands:

```sh
$ flatpak install flathub org.freedesktop.Sdk.Extension.rust-stable
$ flatpak install flathub org.freedesktop.Sdk.Extension.llvm15
```

This will install the Rust and LLVM SDK extensions.

## Enabling SDK Extensions

After installing SDK extensions, you will need to enable them. To do this, set the `FLATPAK_ENABLE_SDK_EXT` environment variable to a comma-separated list of extension names. For example:

```sh
$ FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm15 flatpak run @FLATPAK_ID@
```

This will add compilers, language servers, and other tools to your $PATH.

## Checking Language Server Detection

To check which language servers have been detected, run Helix with the --health option:

```sh
$ FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm15 flatpak run @FLATPAK_ID@ --health
```

You can also get information about a specific language:

```sh
$ FLATPAK_ENABLE_SDK_EXT=rust-stable,llvm15 flatpak run @FLATPAK_ID@ --health rust
```

## Making Changes Persistent

To make changes to the environment variables persistent, use the flatpak override command:

```sh
$ flatpak override --user @FLATPAK_ID@ --env=FLATPAK_ENABLE_SDK_EXT="rust-stable,llvm15"
```

## Finding Other SDK Extensions

To find other SDK extensions, use the following command:

```sh
$ flatpak search <TEXT>
```