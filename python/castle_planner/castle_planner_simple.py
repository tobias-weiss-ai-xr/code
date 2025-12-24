#!/usr/bin/env python3
"""
Castle Building Planner using PAL MCP Server (Simplified)

This script uses the PAL MCP server's planner tool to create a comprehensive
plan for building a castle in Blender, including architecture, modeling techniques,
materials, lighting, rendering, and workflow organization.
"""

import json
import os
import sys
import asyncio

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

async def call_planner_tool():
    """Call the planner tool to create a castle building plan"""

    # Import necessary modules
    try:
        from server import configure_providers, TOOLS
        from utils.model_context import ModelContext
        from providers.registry import ModelProviderRegistry

        # Configure providers first
        configure_providers()
    except Exception as e:
        print(f"Error importing/configuring modules: {e}")
        return

    # Get the planner tool
    if "planner" not in TOOLS:
        print("Error: Planner tool not found in available tools")
        print(f"Available tools: {list(TOOLS.keys())}")
        return

    planner_tool = TOOLS["planner"]

    print("Creating comprehensive plan for building a castle in Blender...")
    print("=" * 70)

    try:
        # Get available models
        available_models = list(ModelProviderRegistry.get_available_models(respect_restrictions=True).keys())
        if not available_models:
            print("No models available. Please configure providers first.")
            return

        model_name = available_models[0]
        print(f"Using model: {model_name}")

        # Create model context
        model_context = ModelContext(model_name)

        # Step 1: Initial planning step - project overview and scope
        step1_params = {
            "step": "I need to create a comprehensive plan for building a detailed medieval castle in Blender. This will include: 1) Castle architecture and design elements (walls, towers, keep, gates, battlements), 2) Blender modeling techniques and workflow (blocking out, detailed modeling, modular design), 3) Materials and texturing strategy (stone, wood, metal, weathering), 4) Lighting and rendering setup (day/night cycles, atmospheric lighting), 5) Timeline and workflow organization (phased approach, asset management). The goal is to create a realistic, detailed castle that could be used for games, animation, or architectural visualization.",
            "step_number": 1,
            "total_steps": 8,
            "next_step_required": True,
            "model": model_name,
            "_model_context": model_context,
            "_resolved_model_name": model_name,
        }

        print("\nSTEP 1: Project Overview and Scope Definition")
        print("-" * 50)

        result1 = await planner_tool.execute(step1_params)

        if result1 and len(result1) > 0:
            response1 = result1[0].text if hasattr(result1[0], "text") else str(result1[0])
            print("Step 1 completed successfully")

            # Parse response to get continuation_id
            try:
                response1_data = json.loads(response1)
                continuation_id = response1_data.get("continuation_id")

                if response1_data.get("status") == "pause_for_deep_thinking":
                    print("\nDEEP THINKING REQUIRED - Complex plan detected!")
                    print("The planner requires deep analysis for this comprehensive castle project.")
                    print(response1_data.get("next_steps", ""))

                print(f"\nPlanner Response: {response1_data.get('step_content', 'No content')[:300]}...")

            except json.JSONDecodeError:
                print(f"Raw response: {response1[:500]}...")
                continuation_id = None
        else:
            print("Step 1 failed - no response received")
            return

        # Step 2: Castle architecture and design elements
        if continuation_id:
            step2_params = {
                "step": "Based on the project scope, I'll now detail the castle architecture and design elements. This includes: 1) Main castle components (keep/citadel, curtain walls, corner towers, gatehouse, barbican, moat), 2) Architectural styles (Romanesque, Gothic, military fortress features), 3) Structural elements (battlements, crenellations, machicolations, arrow slits, murder holes), 4) Interior spaces (great hall, chambers, kitchens, chapel, dungeons), 5) Defensive features (drawbridge, portcullis, gate defenses). Each component needs historical accuracy and structural plausibility.",
                "step_number": 2,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 2: Castle Architecture and Design Elements")
            print("-" * 50)

            result2 = await planner_tool.execute(step2_params)

            if result2 and len(result2) > 0:
                response2 = result2[0].text if hasattr(result2[0], "text") else str(result2[0])
                print("Step 2 completed successfully")

                try:
                    response2_data = json.loads(response2)
                    print(f"\nArchitecture Planning: {response2_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response2[:500]}...")
            else:
                print("Step 2 failed - no response received")
                return

        # Step 3: Blender modeling techniques and workflow
        if continuation_id:
            step3_params = {
                "step": "Now planning the Blender modeling techniques and workflow: 1) Blocking out phase (primitive shapes, scale proportions, basic layout), 2) Modular modeling approach (create reusable assets like wall sections, towers, windows), 3) Detailed modeling techniques (subdivision surface, sculpting details, normal maps), 4) Optimization strategies (LOD levels, efficient topology, texture atlases), 5) Workflow organization (naming conventions, collection management, layering). The approach should balance detail with performance considerations.",
                "step_number": 3,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 3: Blender Modeling Techniques and Workflow")
            print("-" * 50)

            result3 = await planner_tool.execute(step3_params)

            if result3 and len(result3) > 0:
                response3 = result3[0].text if hasattr(result3[0], "text") else str(result3[0])
                print("Step 3 completed successfully")

                try:
                    response3_data = json.loads(response3)
                    print(f"\nModeling Workflow: {response3_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response3[:500]}...")
            else:
                print("Step 3 failed - no response received")
                return

        # Step 4: Materials and texturing strategy
        if continuation_id:
            step4_params = {
                "step": "Planning the materials and texturing strategy: 1) Material categories (stone types - granite, limestone, sandstone; wood varieties - oak, pine; metals - iron, bronze), 2) Texture creation workflow (PBR materials, height maps, normal maps, ambient occlusion), 3) Weathering and aging techniques (cracks, moss, water stains, wear patterns), 4) UV unwrapping strategies (modular UVs, texture atlasing, efficient UV layout), 5) Shader setup (Blender Shader Editor, procedural materials, material nodes). Each material should reflect historical construction methods and environmental exposure.",
                "step_number": 4,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 4: Materials and Texturing Strategy")
            print("-" * 50)

            result4 = await planner_tool.execute(step4_params)

            if result4 and len(result4) > 0:
                response4 = result4[0].text if hasattr(result4[0], "text") else str(result4[0])
                print("Step 4 completed successfully")

                try:
                    response4_data = json.loads(response4)
                    print(f"\nMaterials Strategy: {response4_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response4[:500]}...")
            else:
                print("Step 4 failed - no response received")
                return

        # Step 5: Lighting and rendering setup
        if continuation_id:
            step5_params = {
                "step": "Planning lighting and rendering setup: 1) Lighting scenarios (daylight - sun position, cloud shadows; nighttime - torches, moonlight; atmospheric - fog, volume lighting), 2) Light types and placement (area lights, point lights, spotlights, HDRI lighting), 3) Shadow configuration (shadow mapping, cascade shadows, contact shadows), 4) Rendering settings (Cycles vs Eevee, sampling settings, denoising), 5) Camera work (camera angles, focal lengths, depth of field, animation paths). The lighting should enhance the castle's mood and architectural features.",
                "step_number": 5,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 5: Lighting and Rendering Setup")
            print("-" * 50)

            result5 = await planner_tool.execute(step5_params)

            if result5 and len(result5) > 0:
                response5 = result5[0].text if hasattr(result5[0], "text") else str(result5[0])
                print("Step 5 completed successfully")

                try:
                    response5_data = json.loads(response5)
                    print(f"\nLighting Plan: {response5_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response5[:500]}...")
            else:
                print("Step 5 failed - no response received")
                return

        # Step 6: Timeline and project organization
        if continuation_id:
            step6_params = {
                "step": "Creating timeline and workflow organization: 1) Project phases (Research & Reference → Blocking Out → Detailed Modeling → Texturing → Lighting → Rendering → Post-Processing), 2) Time allocation per phase (realistic estimates based on complexity), 3) Asset management system (file organization, naming conventions, version control), 4) Quality control checkpoints (milestone reviews, technical validation), 5) Final deliverables (still renders, animation sequences, optimization for target platforms). The timeline should accommodate both creative exploration and technical requirements.",
                "step_number": 6,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 6: Timeline and Project Organization")
            print("-" * 50)

            result6 = await planner_tool.execute(step6_params)

            if result6 and len(result6) > 0:
                response6 = result6[0].text if hasattr(result6[0], "text") else str(result6[0])
                print("Step 6 completed successfully")

                try:
                    response6_data = json.loads(response6)
                    print(f"\nTimeline Planning: {response6_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response6[:500]}...")
            else:
                print("Step 6 failed - no response received")
                return

        # Step 7: Technical specifications and optimization
        if continuation_id:
            step7_params = {
                "step": "Technical specifications and optimization planning: 1) Polygon budget management (target poly counts for different components), 2) Texture optimization (resolution settings, compression formats, memory usage), 3) Level of Detail (LOD) strategy (multiple detail levels for different viewing distances), 4) Performance considerations (draw calls, material batching, physics collision), 5) Export settings (file formats, scale conventions, engine-specific requirements). This ensures the castle performs well in various applications while maintaining visual quality.",
                "step_number": 7,
                "total_steps": 8,
                "next_step_required": True,
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 7: Technical Specifications and Optimization")
            print("-" * 50)

            result7 = await planner_tool.execute(step7_params)

            if result7 and len(result7) > 0:
                response7 = result7[0].text if hasattr(result7[0], "text") else str(result7[0])
                print("Step 7 completed successfully")

                try:
                    response7_data = json.loads(response7)
                    print(f"\nTechnical Planning: {response7_data.get('step_content', 'No content')[:300]}...")
                except json.JSONDecodeError:
                    print(f"Raw response: {response7[:500]}...")
            else:
                print("Step 7 failed - no response received")
                return

        # Step 8: Final summary and next steps
        if continuation_id:
            step8_params = {
                "step": "Final step: Comprehensive castle building plan summary. This plan covers all aspects of creating a detailed medieval castle in Blender: architectural design based on historical examples, systematic modeling workflow using modular techniques, comprehensive material and texturing strategies, professional lighting and rendering setups, realistic timeline with proper project organization, and technical optimization for various use cases. The plan provides a complete roadmap from concept to final renders, with specific techniques, tools, and workflows for each phase. Success criteria include historical accuracy, visual quality, technical performance, and efficient workflow management.",
                "step_number": 8,
                "total_steps": 8,
                "next_step_required": False,  # Final step
                "continuation_id": continuation_id,
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
            }

            print("\nSTEP 8: Final Plan Summary and Completion")
            print("-" * 50)

            result8 = await planner_tool.execute(step8_params)

            if result8 and len(result8) > 0:
                response8 = result8[0].text if hasattr(result8[0], "text") else str(result8[0])
                print("Step 8 completed successfully - Planning complete!")

                try:
                    response8_data = json.loads(response8)

                    if response8_data.get("planning_complete"):
                        print("\nCOMPREHENSIVE CASTLE BUILDING PLAN COMPLETED!")
                        print("=" * 70)
                        print("\nComplete Plan Summary:")
                        print(response8_data.get("plan_summary", "No summary available"))

                        if "output" in response8_data:
                            output = response8_data["output"]
                            if "instructions" in output:
                                print(f"\nFinal Instructions:")
                                print(output["instructions"])

                        print(f"\nStatus: {response8_data.get('status', 'Unknown')}")
                        print(f"Continuation ID: {continuation_id}")
                        print("\nNext Steps: You can now begin implementing the castle building plan!")
                        print("Use the continuation ID to start related planning sessions if needed.")

                    else:
                        print("\nPlanning may not be complete - check response status")

                except json.JSONDecodeError:
                    print(f"Raw final response: {response8}")
            else:
                print("Step 8 failed - no response received")
                return

    except Exception as e:
        print(f"Error executing planner: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main function to run the castle building planner"""
    print("PAL MCP Server - Castle Building Planner")
    print("=" * 50)

    try:
        # Run the async planner
        asyncio.run(call_planner_tool())

    except KeyboardInterrupt:
        print("\n\nPlanning interrupted by user")
    except Exception as e:
        print(f"\nError running planner: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()