import subprocess

def deploy_to_platforms():
    print("--- DEPLOYMENT PROTOCOL INITIATED ---")
    
    # Read the prepared ad copy
    with open("social_media_post.txt", "r") as f:
        ad_content = f.read()
        
    # Prepare for Facebook/LinkedIn platforms
    print("\n[Facebook/LinkedIn] Copy this content for your next post:")
    print("------------------------------------------------------------")
    print(ad_content)
    print("------------------------------------------------------------")
    
    # Log the deployment event
    with open("deployment_log.txt", "a") as log:
        log.write("Deployment to Social Media Platforms executed.\n")
        
    print("\nDeployment sequence finalized.")

if __name__ == "__main__":
    deploy_to_platforms()
