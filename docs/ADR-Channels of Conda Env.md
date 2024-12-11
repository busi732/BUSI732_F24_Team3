# ADR: Using Two Channels (`defaults` and `conda-forge`) in Conda Environment

**Date:** 12-10-2024

**Status:** Accepted

## Context

In our project, we configured the Conda environment to use two channels: `defaults` and `conda-forge`. Channels in Conda act as repositories for packages, and the choice of channels directly affects the availability, compatibility, and stability of the packages used in the environment.

The `defaults` channel, maintained by Anaconda, offers stable, optimized packages for most common use cases. On the other hand, `conda-forge` is a community-driven channel that provides access to a wider range of up-to-date and niche packages that may not yet be available in the `defaults` channel.

## Decision

We decided to include both `defaults` and `conda-forge` channels in our environment configuration to achieve a balance between stability and access to a broader array of tools.

## Reasons for Decision

1. **Stability of Core Dependencies (`defaults`)**:
   - Foundational libraries like NumPy and pandas are optimized for performance and reliability in the `defaults` channel.
   - Relying on `defaults` ensures that essential packages remain stable.

2. **Access to Updated or Niche Packages (`conda-forge`)**:
   - Some of the required packages for our project are either unavailable or outdated in the `defaults` channel.
   - `conda-forge` provides access to cutting-edge and community-maintained packages that meet specific project needs.

3. **Dependency Compatibility**:
   - Combining both channels allows better resolution of complex dependency trees, where some packages may require dependencies from `conda-forge` while others work best with `defaults`.

4. **Community Support (`conda-forge`)**:
   - `conda-forge` offers an extensive range of packages maintained by the community, often supporting the latest Python versions and platforms.

5. **Trade-off Mitigation**:
   - Using both channels reduces the trade-off between package stability and innovation, enabling flexibility for both exploratory development and reliable production environments.

## Consequences

### Positive
- Access to a broader range of packages.
- Reliable and stable core libraries from `defaults`.
- Cutting-edge and specialized packages from `conda-forge`.

### Negative
- Potential for dependency conflicts between channels, requiring manual resolution.
- Slight increase in environment setup complexity.

## Implementation

1. Specify channels in the `environment.yml` file:
   ```yaml
   name: fu24_block2_team3_env
   channels:
     - defaults
     - conda-forge
⚠ Please always make sure that there are two channels appears like that when making changes of Conda Environment files
