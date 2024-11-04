from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from policy_scan import helpers



class ComplianceCheckViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["post"])
    def check_compliance(self, request):
        policy_url = request.data.get("policy_url")
        target_url = request.data.get("target_url")

        if not helpers.validate_urls(policy_url, target_url):
            return Response(
                {"error": "Both policy_url and target_url are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            policy_content = helpers.fetch_and_clean_content(policy_url)
            target_content = helpers.fetch_and_clean_content(target_url)
        except Exception:
            return Response(
                {"error": "Failed to fetch content from provided URLs."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        prompt = helpers.generate_prompt(policy_content, target_content)
        try:
            findings = helpers.get_compliance_findings(prompt)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response({"findings": findings}, status=status.HTTP_200_OK)
